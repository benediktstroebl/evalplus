```python
def eat(number, need, remaining):
    """
    Solves the hungry rabbit problem.
    Args:
        number (int): Number of carrots already eaten.
        need (int): Number of carrots to be eaten.
        remaining (int): Remaining carrots in stock.

    Returns:
        List[int]: [Total eaten carrots, Remaining carrots after eating]
    """
    total_eaten = number + remaining
    if total_eaten >= need:
        return [need, remaining - (need - number)]
    else:
        return [total_eaten, 0]
```