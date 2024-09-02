
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
    planets = {
        'Mercury': 1, 'Venus': 2, 'Earth': 3, 'Mars': 4, 
        'Jupiter': 5, 'Saturn': 6, 'Uranus': 7, 'Neptune': 8
    }
    # check that both planet names are valid
    if planet1 not in planets or planet2 not in planets:
        return ()
    planets = dict(sorted(planets.items(), key=lambda x: x[1]))
    # find the orbit of planet1 and planet2
    # find planets whose orbits are between the orbits of planet1 and planet2
    # sort the result by proximity to the sun
    return tuple(planet[0] for planet in planets.items() 
                 if planets[planet1] < planet[1] < planets[planet2])
    
    # other solution
    # planets = dict(sorted(planets.items(), key=lambda x: x[1]))
    # return tuple(planet[0] for planet in planets.items() 
    #     if planet1 < planet[1] < planet2)

