
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        return (sum(starts_one_ends(n//10)) + starts_one_ends(n%10)) % 2

if __name__ == "__main__":
    # Example usage
    print(starts_one_ends(123456789)) # prints 3
    print(starts_one_ends(12345678)) # prints 2
    print(starts_one_ends(1234)) # prints 1
    print(starts_one_ends(987654321)) # prints 1