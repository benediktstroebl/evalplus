

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # Create a 2D list
    numbers = [[0] * (max(lst) + 1) for _ in range(len(lst))]

    for num in lst:
        # Round num to the ceiling
        num = round(num)

        # Update the 2D list
        numbers[0][num] += 1
        for i in range(1, len(numbers)):
            numbers[i][num] += numbers[i - 1][num]
    
    # Calculate the sum of the squared elements
    result = 0
    for i in range(len(numbers)):
        result += numbers[i][2] ** 2

    # Return the result
    return round(result)