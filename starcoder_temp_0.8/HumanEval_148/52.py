
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    orbits = {
        'Mercury': 0, 
        'Venus': 1, 
        'Earth': 2, 
        'Mars': 3, 
        'Jupiter': 4, 
        'Saturn': 5, 
        'Uranus': 6, 
        'Neptune': 7
    }
    
    if planet1 in orbits and planet2 in orbits:
        index1 = orbits[planet1]
        index2 = orbits[planet2]
        return tuple(sorted([x for x in orbits.keys() if orbits[x] > index1 and orbits[x] < index2]))
    else:
        return tuple([])
