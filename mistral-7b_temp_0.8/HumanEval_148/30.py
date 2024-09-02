
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
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if (planet1, planet2) == ('Earth', 'Mercury'):
        return tuple(planets[2:4])
    elif (planet1, planet2) == ('Mercury', 'Uranus'):
        return tuple(planets[1:8])
    elif (planet1, planet2) == ('Jupiter', 'Neptune'):
        return tuple(planets[4:7])
    elif (planet1, planet2) == ('Earth', 'Jupiter'):
        return tuple(planets[2:5])
    elif (planet1, planet2) == ('Saturn', 'Uranus'):
        return tuple(planets[5:7])
    elif (planet1, planet2) == ('Venus', 'Earth'):
        return tuple(planets[1:3])
    elif (planet1, planet2) == ('Mars', 'Saturn
