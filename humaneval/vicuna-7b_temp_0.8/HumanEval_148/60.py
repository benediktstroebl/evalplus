
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
    # check if the planets are valid
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if planet1 == planet2:
        return []
    
    # check the proximity of each planet to the sun
    proximity = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, 9):
        for j in range(i+1, 9):
            if i != j:
                proximity[i] = abs(planet1.semi_major_axis - planet2.semi_major_axis)
                proximity[j] = abs(planet2.semi_major_axis - planet1.semi_major_axis)
    
    # create a list of planets
    planets = []
    for i in range(1, 9):
        for j in range(i+1, 9):
            if i != j:
                if proximity[i] < proximity[j]:
                    planets.append(planet1)
                elif proximity[j] < proximity[i]:
                    planets.append(planet2)
                elif proximity[i] == proximity[j]:
                    planets.append(f"{planet1} and {planet2}")
                else:
                    planets.append(f"{planet1} or {planet2}")
    
    # sort the planets by proximity to the sun
    planets = sorted(planets, key=lambda x: x[0], reverse=True)
    
    return planets
