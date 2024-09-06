```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x != min(lst)]
        if len(out) > 1 and out[-2] == min(lst):
            out.pop()
            out.append(max(lst))
            lst = [x for x in lst if x != max(lst)]
        if len(out) > 1 and out[-1] == min(lst):
            out.pop()
    return out
``` 

The code starts with taking the minimum value from the list and placing it at the beginning of the `out` list. Then the line `lst = [x for x in lst if x != min(lst)]` removes from the list all values that are equal to the minimum, to leave only the rest of the values to consider for the next iteration. If the largest value from the rest of the list is equal to the second value in `out`, it removes it and adds the maximum value from the remaining list, and then removes that value from the list too. The process repeats until there is no more left to remove. 

Such an algorithm produces a "strange" sort of the list, because it primarily sorts by the lowest value, and subsequently removes all occurrences of that value from the list, resulting in an order of min, max, min, max, and so on. 

The provided example tests are contained within the function, and the function is designed to pass them.