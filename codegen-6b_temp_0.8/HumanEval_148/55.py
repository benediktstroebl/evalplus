
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
    planets = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune'
        ]
    if planet1 in planets and planet2 in planets:
        planet1Home = index(planet1, planets)
        planet2Home = index(planet2, planets)
        planetHomes = sorted([planet1Home, planet2Home])
        planetLists = [planets[planetHomes[i]-1:planetHomes[i+1]] for i in range(0, len(planetHomes)-1, 2)]
        return tuple(list(itertools.chain.from_iterable(planetLists)))
    else:
        return tuple()
