# def minimize_cost(x, y):
#     """
#     Minimizes the objective function z = 120x + 80y subject to constraints.

#     Args:
#         x: Integer value for variable x.
#         y: Integer value for variable y.

#     Returns:
#         True if a feasible solution is found, False otherwise.
#     """

#     # Check if constraints are met
#     if (2 * x + y > 6 or
#         7 * x + 8 * y > 28 or
#         x < 0 or
#         y < 0):
#         return False

#     # Calculate objective function value
#     z = 120 * x + 80 * y

#     # Print the solution
#     print(f"x = {x}, y = {y}, z = {z}")
#     return True


# while True:
#     # Get user input for x and y
#     while True:
#         try:
#             x = int(input("Enter an integer value for x: "))
#             y = int(input("Enter an integer value for y: "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter integers only.")

#     # Check constraints and minimize cost
#     if minimize_cost(x, y):
#         print("Feasible solution found!")
#     else:
#         print("Constraints not met. No feasible solution found.")

#     # Ask if user wants to continue
#     user_choice = input("Do you want to solve another problem? (y/n) ")
#     if user_choice.lower() != "y":
#         break

# print("Exiting program.")


# """
# formulate the LP:
# That is, give the objective function and constraints.
# a farmer operates a large farm on which sheeps are raised. he is considering 3 different grains to feed the sheep. the table lists the number of
# units of each nutrients in ach lb of grain, the minimum daily requirement at each nutrient for each sheep and the cost of each grain. the farmer wants to raise the sheeps at MINIMUM COST.

# nutrient      grain         min daily requirement

#             1   2   3           (units)
# a           20  30  70            110
# b           10  10  0             18
# c           50  30  0             90
# d           6   2.5 10            40
# cost$       41  36  96S
# """


def maxnum(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value


print(maxnum([10, 20, 30]))
