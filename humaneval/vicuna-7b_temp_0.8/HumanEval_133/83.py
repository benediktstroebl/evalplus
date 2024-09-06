

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
    def is_int(val):
        """Check if val is an integer
        

        :param val:
        :return: True if val is an integer, False otherwise
        

        """
        return not val or val.isdigit()

    def round_upper(val):
        """Round a number to the nearest integer
        

        :param val:
        :return: The nearest integer
        :rtype: int
        

        """
        return int(val * 10)

    def sum_of_squares(lst):
        """Calculate the sum of squared elements in the list
        

        :param lst:
        :return: The sum of squared elements in the list
        :rtype: float
        

        """
        n = len(lst)
        s = 0
        for i in range(n):
            val = lst[i]
            if is_int(val):
                s += val ** 2
            else:
                s += val * (val - int(val))
        return round_upper(s)

    return sum_of_squares(lst)
