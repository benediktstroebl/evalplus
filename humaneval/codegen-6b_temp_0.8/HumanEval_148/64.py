
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
    planets = {'Mercury': [0, 'Mercury', [0]], 'Venus': [0, 'Venus', [0]], 'Earth': [0, 'Earth', [0]],
               'Mars': [0, 'Mars', [0]], 'Jupiter': [0, 'Jupiter', [0]], 'Saturn': [0, 'Saturn', [0]],
               'Uranus': [0, 'Uranus', [0]], 'Neptune': [0, 'Neptune', [0]]}
    planets[planet1][2][0] = 1
    planets[planet2][2][0] = 1
    planets[planet1][2].sort()
    planets[planet2][2].sort()
    temp = []
    for index in planets[planet1][2]:
        for index2 in planets[planet2][2]:
            if index + index2 == 2:
                temp.append(planets[index][1])
    temp.sort()
    return tuple(temp)

