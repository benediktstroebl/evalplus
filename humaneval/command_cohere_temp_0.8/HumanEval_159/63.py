Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    if n + need > rem:
        return [rem, 0]
    else:
        return [n + need, rem - (n + need)]
```
This script defines a function 'eat' which takes in three variables need, remaining, and consumed carrot counts. It returns a list [total consumed after eating, remaining carrots after eating]. The function will return [remaining, 0] if there are not enough carrots to fulfill the 'need'. If there are enough, it will return the total consumed after eating and the remaining count after eating. 

This function can be used to solve the problem statement provided. Let's dig deeper into the code and explain it step by step below:
```
1. If Statement:
    * This code first checks if the total number of carrots eaten plus the number of carrots to be eaten will exceed the total number of remaining carrots. In other words, it checks if there are not enough carrots to take in the full 'need' amount. This is done because the function will return the remaining amount of carrots after eating in this case, which will be zero (as you have eaten the total remaining). This checks if rem <= n + need.

2. Return Statement 1:
    * If the condition above is true, the function will return a list [rem, 0], meaning the total amount eaten is the total remaining, and there are zero carrots remaining.

3. Else Statement:
    * If the condition above is false, the function will return the amount of carrots eaten plus the amount of carrots to be eaten, and the amount of carrots remaining (after eating). This is listed as [n + need, rem - (n + need)], meaning the total carrots eaten/taken in, and the remaining amount of carrots after eating.
```

This function will work for any 0 <= n <= 1000, 0 <= need <= 1000, and 0 <= remaining <= 1000. Thus, it fulfills the constraint you provided. I hope this helps explain the code! Let me know if you would like to discuss the problem statement or the code solution further.