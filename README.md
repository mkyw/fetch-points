Fetch Coding Exercise - Points per payer tracker

This program takes two arguments -- a csv file containing payer, points, and timestamp, and a points requested input, and evaluates how the points should be spended, given the fact that older points based on timestamp should be spent first, and no payer's total points should become negative.

The program takes all the inputs and sort it into a stack in increasing order of the timestamp, and consumes each instance, considering the points against the points requested as well as the payer's total points. The leftover points from each payer is printed after the transaction is executed.

To call the program, run python3 mycode.py [number of points] [csv_file.csv], where each argument should be filled with the desired value and file location.