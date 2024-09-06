
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
    if not is_valid_planet_name(planet1) or not is_valid_planet_name(planet2):
        return []
    
    if planet1 > planet2:
        temp = planet1
        planet1 = planet2
        planet2 = temp
    planets = [planet1, planet2]
    for p1 in planets:
        for p2 in planets:
            if p1 < p2:
                if abs(p1 - planet2) < abs(p2 - planet1):
                    print(p2)
                    break
        else:
            print("")
    
    return sorted(planets, key=lambda x: abs(x - planet2), reverse=True)

example = [("Saturn", "Uranus"), ("Jupiter", "Mars"), ("Venus", "Earth")]
result = bf(*example[0])
print(result)