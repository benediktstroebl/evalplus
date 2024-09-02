
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    string_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def number_to_letter(num):
        """
        Helper function that converts an integer to a string
        """
        for key, value in string_to_num.items():
            if num == value:
                return key

    def letter_to_number(letter):
        """
        Helper function that converts a letter to an integer
        """
        for key, value in string_to_num.items():
            if letter == key:
                return value

    def number_to_letter_arr(num_arr):
        """
        Helper function that converts an array of integers to an array of strings
        """
        result_arr = []
        for num in num_arr:
            result_arr.append(number_to_letter(num))

        return result_arr

    def letter_to_number_arr(letter_arr):
        """
        Helper function that converts an array of strings to an array of integers
        """
        result_arr = []
        for letter in letter_arr:
            result_arr.append(letter_to_number(letter))

        return result_arr

    def digit_to_string(arr):
        """
        Main function that converts an array of integers to an array of strings
        """
        result_arr = []
        # Convert the array of integers to an array of strings
        for num in arr:
            # If the number is between 1 and 9, add its corresponding letter to the result
            if num in range(1, 10):
                result_arr.append(number_to_letter(num))
            # If the number is 0 or any other number, ignore it
            else:
                pass

        # Reverse the array
        result_arr = result_arr[::-1]

        # Convert
