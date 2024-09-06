
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def count_nums(n):
        """
        Return a list containing the count of each digit 1-9 in the string form of
        n-digit positive integers.
        """
        def char_num(n):
            """
            Return the number of characters in the string representation of
            the integer n.
            """
            return len(str(n))
        nums = [0] * 10
        for i in range(1, n):
            digits = char_num(i)
            if digits == 1:
                nums[1] += 1
            elif digits == 2:
                nums[2] += 1
                nums[2] += 1
            elif digits == 3:
                nums[3] += 1
                nums[3] += 1
                nums[3] += 1
            elif digits == 4:
                nums[4] += 1
                nums[4] += 1
                nums[4] += 1
                nums[4] += 1
            elif digits == 5:
                nums[5] += 1
                nums[5] += 1
                nums[5] += 1
                nums[5] += 1
                nums[5] += 1
            elif digits == 6:
                nums[6] += 1
                nums[6] += 1
                nums[6] += 1
                nums[6] += 1
                nums[6] += 1
                nums[6] += 1
            elif digits == 7:
                nums[7] += 1
                nums[7] += 1
                nums[7] += 1
                nums[7] += 1
                nums[7] += 1
                nums[7] += 1
                nums[7] += 1
            elif digits == 8:
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
                nums[8] += 1
            elif digits == 9:
