
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

    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    elif planet1 == 'Mercury':
        return tuple(x for x in planets if x != planet2 and x != 'Mercury')
    elif planet2 == 'Neptune':
        return tuple(x for x in planets if x != planet1 and x != 'Neptune')
    else:
        return tuple(x for x in planets if x != planet1 and x != planet2 and x != 'Mercury' and x != 'Neptune')
