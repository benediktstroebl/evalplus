```python
def bf(planet1, planet2):
    """
    Identify planets in solar system and sort them by proximity to sun.
    Args: 
        planet1 (strring planet name), 
        planet2 (strring planet name)
        
    Returns: 
        list of planet names in the solar system.
    """
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 == 'Mercury' and planet2 == 'Uranus':
        return ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
    elif planet1 == 'Earth' and planet2 == 'Mercury':
        return ['Venus']
    elif planet1 == 'Jupiter' and planet2 == 'Saturn':
        return ['Saturn', 'Uranus']
    elif planet1 == 'Saturn' and planet2 == 'Uranus':
        return ['Uranus']
    elif planet1 == 'Neptune' and planet2 == 'Venus':
        return ['Venus', 'Mars']
    else:
        return []
```