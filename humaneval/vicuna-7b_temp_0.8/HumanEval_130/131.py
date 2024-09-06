
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    # Create a list to store the first n+1 numbers
    # Push 3 to the list, which is the first number of Tribonacci sequence
    numbers = [3]
    # Push the number n/2 to the list, because Tribonacci sequence starts with 1 and 
    # every odd number is the sum of the previous two even numbers
    numbers.append(n//2)
    # Check if n is even or odd
    if n%2 == 0:
        # If n is even, just append the numbers to the list
        numbers.append(n)
    else:
        # If n is odd, use the recurrence relation to calculate the first n+1 numbers
        for i in range(1, n+1):
            numbers.append(numbers[i-1] + numbers[i-2] + numbers[i])
    return numbers
