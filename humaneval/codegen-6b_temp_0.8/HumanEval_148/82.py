
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
    # your code here
    planets = ('Jupiter', 'Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Uranus', 'Neptune')
    plant1, plant2 = 'Earth', 'Venus'
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    else:
        planet1 = planets.index(planet1)
        planet2 = planets.index(planet2)
        return (
                planets[(planet1 + 1) % 8],
                planets[(planet1 + 2) % 8],
                planets[(planet1 + 3) % 8],
                planets[(planet1 + 4) % 8],
                planets[(planet1 + 5) % 8],
                planets[(planet1 + 6) % 8],
                planets[(planet1 + 7) % 8],
                planets[(planet2 - 1) % 8],
                planets[(planet2 - 2) % 8],
                planets[(planet2 - 3) % 8],
                planets[(planet2 - 4) % 8],
                planets[(planet2 - 5) % 8],
                planets[(planet2 - 6) % 8],
                planets[(planet2 - 7) % 8],
                planets[(planet2 - 8) % 8],
                planets[(planet2 - 9) % 8]
            )

