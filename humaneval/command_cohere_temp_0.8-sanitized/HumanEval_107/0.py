def even_odd_palindrome(n):
    """
    This function calculates the number of even and odd integer palindromes in the range(1, n+1) and returns a tuple containing these counts.
    """

    # Initializing the count of even and odd palindromes to 0
    even_count = 0
    odd_count = 0
    
    # The following loop calculates the number of even and odd palindromes based on the input number n
    for num in range(1, n+1):
        # Checking if the current number is a palindrome by comparing the first and last digits
        if num == int(str(num)[0] + str(num)[-1]):
            # If the number is a palindrome, incrementing the respective count based on its parity
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    # Returning the calculated counts as a tuple
    return (even_count, odd_count)
n = int(input("Enter a number: "))