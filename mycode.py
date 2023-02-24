import csv
import operator
import sys


def main():
    # Set up variables, points is the number of points to be spent
    # stack is the csv list, payers is a running total of each payer
    points = int(sys.argv[1])
    stack = list()
    payers = dict(set())

    # Reads the file and inserts each row of the csv file into a dict
    # and sorts the list based on the timestamp
    # Initialize the payers variable, keeping each payer key unique
    with open(sys.argv[2], 'r') as file:
        csvreader = csv.DictReader(file)

        stack = list(csvreader)
        stack.sort(key=operator.itemgetter('timestamp'))

        for i in stack:
            if payers.get(i['payer']):
                payers[i['payer']] = payers.get(
                    i['payer']) + int(list(i.values())[1])
            else:
                payers.update({i['payer']: int(list(i.values())[1])})

    # Make sure the account has enough points to fulfill point request
    totalpoints = 0
    for i in payers:
        totalpoints += payers[i]

    if points > totalpoints:
        print("Not enough points!")
        return

    # Running total of points taken from each payer, goal to equal points variable
    current = 0

    # While the points total has not been met, continue to pop each payer with the
    # from the earliest timestamp from the top of the stack
    while current < points:
        d = stack.pop(0)
        d_key = list(d.values())[0]
        d_value = int(list(d.values())[1])

        # Each time we subtract points from payers we check whether the total points
        # for a player will become negative

        # if the new payer instance exceeds the points total, we only need partial
        # points from this instance of the payer
        if current + d_value > points and payers[d_key] >= points - current:
            d_value = d_value - points + current
            current = points
            d["points"] = d_value
            payers[d_key] = d_value
            stack.insert(0, d)  # reinsert unused points into stack

        # if the new payer instance does not exceed points total, we consume all the
        # points in the instance
        elif payers[d_key] >= d_value or payers[d_key] - d_value > 0:
            payers[d_key] -= d_value
            current += d_value

        # if the payer does not have enough points, we subtract points and send the payers account to 0
        # and reenter the remainder into the stack. if there are negative points from the payer later,
        # such as in the example, it would free up the positive points to be used.
        else:
            current += payers[d_key]

            d["points"] = d_value - payers[d_key]
            stack.insert(1, d)

            payers[d_key] = 0

    print(payers)
    return payers


if __name__ == "__main__":
    main()
