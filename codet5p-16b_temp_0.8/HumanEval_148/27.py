
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

    import math
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    
    orbit_r = dict(zip(planets, [3871, 6047, 9686, 3390, 69911, 66851, 42828, 13906]))
    center = orbit_r[planet1]
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    count = 0
    pairs = []
    if planet2_index < planet1_index:
        while planet2_index > planet1_index:
            planet2_index -= 1
            count += 1
            pairs.append(planets[planet2_index])
        
        while count < abs(planet1_index - planet2_index):
            planet2_index += 1
            count += 1
            pairs.append(planets[planet2_index])
    
