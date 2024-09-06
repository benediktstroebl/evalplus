
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
    if not isinstance(planet1,str)or not isinstance(planet2,str):
        return ()
    if planet1.lower() not in ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']:
        return ()
    if planet2.lower() not in ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']:
        return ()
    orbits = [2.067e11,1.496e11,1.000e10,7.149e9,4.638e9,3.026e9,1.425e9]
    distance = []
    for p in (planet1, planet2):
        # Check if planet is within the correct range
        if p not in ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']:
            return ()
        distance.append(orbits[orbits.index(p)+1]-orbits.index(p)+1)
    return distance

print(bf('Earth','Mars'))
