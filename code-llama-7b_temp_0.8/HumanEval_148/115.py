
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
    planetList = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn',
                  'Uranus', 'Neptune']
    planetIndexList = [0, 1, 2, 3, 4, 5, 6, 7]
    index1 = planetList.index(planet1)
    index2 = planetList.index(planet2)
    planetList = planetList[index1:index2+1]
    planetIndexList = planetIndexList[index1:index2+1]
    sortedPlanets = [planetList[index] for index in sorted(planetIndexList)]
    return sortedPlanets
