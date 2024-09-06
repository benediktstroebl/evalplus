def even_odd_palindrome(n):
    # Ensure n is a positive integer
    if n <= 0:
        return "Invalid input for n. Please input a positive integer."

    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Create a reversed counterpart of i as a string
        reversed_i = str(i)
        reversed_i = reversed_i[::-1]
        
        # Check if the two counterparts are equal to determine if it's a palindrome
        if i == int(reversed_i):
            if len(reversed_i) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
n = int(input("Enter a positive integer: "))