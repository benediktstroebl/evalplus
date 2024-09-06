
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
    data = [('Mercury', '2.3e11'), ('Venus', '2.6e11'), ('Earth', '3.0e11'),
    ('Mars', '3.1e11'), ('Jupiter', '5.2e11'), ('Saturn', '9.6e11'),
    ('Uranus', '2.8e12'), ('Neptune', '4.5e12'), ('Pluto', '7.4e12')]
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn',
    'Uranus', 'Neptune', 'Pluto']
    if planet1 in planets and planet2 in planets:
        i = planets.index(planet1)
        j = planets.index(planet2)
        if i <= j:
            return tuple(planets[i:j + 1])
        else:
            return tuple(planets[i:j])
    else:
        return tuple()
