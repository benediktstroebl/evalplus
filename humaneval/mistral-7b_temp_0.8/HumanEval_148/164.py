
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
    planets = planets[0:4] + [x + ' II' for x in planets[4:]]

    planet1 = 'Mercury'
    planet2 = 'Neptune'
    #data = []
    for i in planets:
        if i in planets[0:4]:
            if i in planet1:
                if i in planet2:
                    data.append(i)
        if i in planets[4:]:
            if i in planet1:
                if i not in planet2:
                    data.append(i)

    if planet1 == planet2:
        return []
    else:
        return tuple(data)


