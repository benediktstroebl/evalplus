```python
def number_of_odd_digits(string_list):
    odd_count_dict = {}
    for string in string_list:
        odd_count = sum(1 for char in string if char % 2 != 0)
        odd_count_dict[string] = odd_count
    output_list = [f"the number of odd elements {odd_count}n the str{len(string)}g {string} of the input."
                   for string, odd_count in odd_count_dict.items()]
    return output_list

# Test Cases
>>> odd_count(['1234567'])
["the number of odd elements 4n the str4ng 4 of the 4nput."]
>>> odd_count(['3',"11111111"])
["the number of odd elements 1n the str1ng 1 of the 1nput.",
"the number of odd elements 8n the str8ng 8 of the 8nput."]
```

The function uses a dictionary to store the odd count for each string. The lambda function sums up the number of odd digits in each string using a generator expression. Each digit is checked for parity using the modulus operator (`char % 2 != 0`). The dictionary keys are the input strings, and the values are the corresponding counts of odd digits. The output list is then created by replacing `n` with the string length and `odd_count` with the value from the dictionary.