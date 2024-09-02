
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
    # write your code here

    listOfPlanets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if (planet1 not in listOfPlanets) or (planet2 not in listOfPlanets):
        return ()

    if planet1 == planet2:
        return planet1

    if planet1 == 'Mercury' and planet2 == 'Neptune':
        return listOfPlanets

    if planet1 == 'Mercury' and planet2 != 'Neptune':
        return listOfPlanets[:planet2]

    if planet2 == 'Mercury' and planet1 != 'Neptune':
        return listOfPlanets[planet1:]

    if planet1 > planet2:
        tmp = planet1
        planet1 = planet2
        planet2 = tmp

    return listOfPlanets[listOfPlanets.index(planet1)+1:listOfPlanets.index(planet2)]

