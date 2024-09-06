
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
    # If n is even, we can just return the first two numbers
    if n//2 == 0:
        return [3, n]
    # If n is odd, we can use the recurrence relation to calculate the first n + 1 numbers
    else:
        result = [n, n//2, n//3]
        # Keep track of the number of Tribonacci numbers we've calculated
        count = 1
        # Calculate the next n + 1 numbers
        for i in range(2, n+1):
            # If the current number is odd, add the two previous numbers
            if i % 2 == 1:
                result.append(result[count-1] + result[count-2] + result[count-3])
            # Increment the count
            count += 1
        return result
