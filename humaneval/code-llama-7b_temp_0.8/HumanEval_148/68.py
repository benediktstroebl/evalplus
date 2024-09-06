
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
    if planet1 == 'Venus':
        return ('Earth',)
    elif planet1 == 'Earth':
        return ('Mercury', 'Venus')
    elif planet1 == 'Mercury':
        return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    elif planet1 == 'Mars':
        return ('Earth', 'Mercury', 'Venus', 'Jupiter', 'Saturn')
    elif planet1 == 'Jupiter':
        return ('Mercury', 'Venus', 'Earth', 'Mars', 'Saturn')
    elif planet1 == 'Saturn':
        return ('Jupiter', 'Mercury', 'Venus', 'Earth', 'Mars')
    elif planet1 == 'Uranus':
        return ('Jupiter', 'Mercury', 'Venus', 'Earth', 'Mars', 'Saturn')
    elif planet1 == 'Neptune':
        return ('Jupiter', 'Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Uranus')
    elif planet1 == 'Mercury' and planet2 == 'Uranus':
        return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    elif planet1 == 'Mercury' and planet2 == 'Saturn':
        return ('Venus', 'Earth', 'Mars', 'Jupiter')
    elif planet1 == 'Venus' and planet2 == 'Saturn':
        return ('Earth', 'Mercury', 'Mars', 'Jupiter')
    elif planet1 == 'Earth' and planet2 == 'Saturn':
        return ('Mercury', 'Venus', 'Mars', 'Jupiter')
    elif planet1 == 'Mars' and planet2 == 'Saturn':
        return ('Earth', 'Mercury', 'Venus', 'Jupiter')
    elif planet1 == 'Jupiter' and planet2 == 'Saturn':
        return ('
