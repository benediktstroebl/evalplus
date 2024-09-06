```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = int(str(num)[0])
            last = int(str(num)[-1])
            if curr % 2 == 1 and last % 2 == 1:
                oddCount += 1
    return oddCount
```

The above code uses a loop to iterate through each element in the input list of numbers (`nums`). For each number, it checks if the number is greater than 10. If so, it calculates if the first digit (obtained by converting the number to a string and extracting the first character) and the last digit (obtained by converting the number to a string and extracting the last character) are both odd (using the modulo operator `% 2 == 1` to check). If both conditions are met, it increments the `oddCount` variable by 1. Finally, it returns the `oddCount` count of numbers meeting this criteria. 

To execute this code you need to save it in a file and run it with Python. The following code will execute the file:
```bash
python your_script_name.py
``` 
It is important to make sure you have the right file name and that the script is saved in the directory you want to execute it from. Pipings the file are not necessary.