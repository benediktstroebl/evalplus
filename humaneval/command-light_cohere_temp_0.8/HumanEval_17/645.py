```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', '.']
    notes = [rating.length for rating in notes]
    
    for i,beat in enumerate(notes):
        rating = notes[beat]
        if beat < 4:
            if rating == '|': beat -= 1
            else: beat -= 2
        else:
            beat -= 4
        yield beat
    
    return []

# Test cases
test_cases = [
    "'.join string(). `o o| .| o| o| .| .| .| o o`
    "`o o| o .o| o| .| o`
    "`o o| o o| . `o `
    ```

test_results = [parse_music(test_case) for test_case in test_cases]
print(test_results)
```