
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
    if planet1 == 'Mercury':
        bf_mercury = ('Venus',)
        return bf_mercury
    elif planet1 == 'Venus':
        bf_venus = ('Earth',)
        return bf_venus
    elif planet1 == 'Earth':
        bf_earth = ('Mars',)
        return bf_earth
    elif planet1 == 'Mars':
        bf_mars = ('Jupiter',)
        return bf_mars
    elif planet1 == 'Jupiter':
        bf_jupiter = ('Saturn',)
        return bf_jupiter
    elif planet1 == 'Saturn':
        bf_saturn = ('Uranus',)
        return bf_saturn
    elif planet1 == 'Uranus':
        bf_uranus = ('Neptune',)
        return bf_uranus
    elif planet1 == 'Neptune':
        bf_neptune = ()
        return bf_neptune
    elif planet1 not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()

    if planet2 == 'Mercury':
        bf_mercury = ('Venus',)
        return bf_mercury
    elif planet2 == 'Venus':
        bf_venus = ('Earth',)
        return bf_venus
    elif planet2 == 'Earth':
        bf_earth = ('Mars',)
        return bf_earth
    elif planet2 == 'Mars':
        bf_mars = ('Jupiter',)
        return bf_mars
    elif planet2 == 'Jupiter':
        bf_jupiter = ('Saturn',)
        return bf_jupiter
    elif planet2 == 'Saturn':
        bf_saturn = ('Uranus',)
        return bf_sat
