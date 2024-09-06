```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_dict = {}
    letters_list = []
    for letter in s:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
        letters_list.append(letters_dict[letter])
    return all(x != 2 for x in letters_list)
```

This Python script defines a function called `is_happy` that takes a string as input and checks if it is happy. 

Here's an explanation of the logic:
1. It starts by checking if the string's length is at least 3, so it returns False immediately if the length is less than 3 because a happy string must have a minimum length of 3.
2. Then it prepares to analyze whether the consecutive counts of letters in the string are distinct. It initializes a dictionary called `letters_dict` to count the occurrences of each letter in the string. 
3. Subsequently, it creates an empty list called `letters_list` to store the consecutive letter counts. It then iterates through each letter in the string, and if the letter is already in the `letters_dict`, its count is incremented; otherwise, it's added to the dictionary with a count of 1.
4. The count of consecutive occurrences for each letter is added to the `letters_list`.
5. Finally, the function checks if each count in `letters_list` is different from 2, and uses the `all()` function to determine if all counts are not equal to 2. If this condition is true, it means that the consecutive letters are distinct, and the string is considered happy; otherwise, it's not happy. 

This script provides an effective and concise solution to the problem statement provided.