def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the case where n equals 1
    if n == 1:
        return 2
    
    # Remove the first and last digits since the number starts and ends with 1
    digits.pop(0)
    digits.pop()
    
    # Combine the digits to form numbers
    numbers = [int('1' + ''.join(map(str, digits)) + '1') for digits in itertools.permutations(digits)]
    
    return len(numbers)