
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Create a new string where the lowercase characters have been replaced by the uppercase version
    upper_str = ''.join(chr(ord(c) - 32) for c in s)
    
    # Use the digits_to_sums function to get the sum of the uppercase characters
    nums = digits_to_sums(upper_str)
    
    # Add the digits of the input string
    return sum(nums)
