
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    "*** YOUR CODE HERE ***"
    
    def digits_of(n):
        """Return list of digits of n.

        >>> digits_of(15)
        [1, 0, 5]
        >>> digits_of(1533)
        [1, 5, 3]
        """
        return list(str(n))

    def even_digits(n):
        """Returns True if n has even digits, False otherwise.

        >>> even_digits(15)
        True
        >>> even_digits(1533)
        False
        """
        return len(digits_of(n)) % 2 == 0

    def remainders(n):
        """Return a list of all values that are less than n mod 10.

        >>> remainders(15)
        [5, 5, 5, 5]
        >>> remainders(1025)
        []
        """
        return [i for i in range(n) if not i % 10]

    def sum_of_remainders(n):
        """
        >>> sum_of_remainders(15)
        120
        >>> sum_of_remainders(1025)
        0
        """
        return sum(remainders(n))

    def all_elements_from_remainders(n):
        """Return a list of numbers between 0 and n that are divisible by n.

        >>> all_elements_from_remainders(1)
        [0]
        >>> all_elements_from_remainders(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        return [i for i in range(sum_of_remainders(n)) if i % n == 0]

    def all_elements_from_remainders(n):
        """Return a list of numbers between 0 and n that are divisible by n.

        >>> all_elements_from_remainders(15)
        [0, 15]
        """

        return [i for i in range(n) if not i % n]

    def sum_of_