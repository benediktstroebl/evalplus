```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for num in reversed_digits:
        names.append(num_to_word(num))
    return names if names else []

def num_to_word(num):
    words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return words.get(num, "")
``` 

The function `by_length` takes an array of integers as input and performs several steps to transform it into a list of named digits, ensuring that strange numbers are ignored. Let's break down the code further:
1. **Sorting:** The integers between 1 and 9 are sorted in ascending order using the `sorted` function.
2. **Filtering:** The sorted array is then filtered to only include the digits (integers from 1 to 9). This is done using a list comprehension, which results in `filtered_digits`.
3. **Reversing:** The filtered digit array is reversed using slicing, resulting in `reversed_digits`.
4. **Replacing with Names:** The reversed digit array is iterated through, and each digit is replaced by its corresponding name using the `num_to_word` helper function. The dictionary `words` assigns each digit a name.
5. **Return Empty Result for Empty or Filtered Array:** The function returns an empty list if the input array is empty or if the filtering process results in an empty array of digits. This is ensured by the condition `names if names else []`. 

The `num_to_word` helper function translates a digit into its respective name, utilizing a dictionary as a lookup mechanism to retrieve the name associated with a given digit.