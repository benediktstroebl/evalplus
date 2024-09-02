
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
    def get_planet(planet):
        return planets[planets.index(planet)]

    planets = ['Venus', 'Jupiter', 'Saturn', 'Uranus', 'Earth', 'Mercury', 'Neptune']

    planet1 = planet1.lower() if planet1.lower() in planets else False
    planet2 = planet2.lower() if planet2.lower() in planets else False

    if not planet1 or not planet2:
        return ()

    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    if planet1_index < planet2_index:
        start_index = planet1_index
        end_index = planet2_index
    else:
        start_index = planet2_index
        end_index = planet1_index
    
    for p1 in planets[start_index:end_index]:
        for p2 in planets[start_index+1:end_index]:
            if get_planet(p1) > get_planet(p2):
                return (p2, p1)
    
    return ()
