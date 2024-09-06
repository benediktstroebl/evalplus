
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
    planet_list = []
    planet_1_index = 0
    planet_2_index = 0
    for i in planets:
        if i == planet1:
            planet_1_index = planets.index(i)
        if i == planet2:
            planet_2_index = planets.index(i)
    if planet_1_index == 0 or planet_2_index == 0:
        return tuple()
    elif planet_1_index < planet_2_index:
        planet_list = planets[planet_1_index + 1:planet_2_index]
    else:
        planet_list = planets[planet_2_index + 1:planet_1_index]
    return tuple(planet_list)
