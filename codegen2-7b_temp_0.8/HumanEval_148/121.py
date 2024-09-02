
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
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    planets_1 = [planet1, planet2]
    planets_2 = [planet2, planet1]
    
    planets_1_dict = {'venus': 'Earth','mars': 'Earth','mercury': 'Earth', 'earth': 'Earth', 
                      'jupiter': 'Earth','saturn': 'Earth', 'uranus': 'Earth', 'neptune': 'Earth'}

    planets_2_dict = {'venus': 'Earth','mars': 'Earth','mercury': 'Earth', 'earth': 'Earth', 
                      'jupiter': 'Earth','saturn': 'Earth', 'uranus': 'Earth', 'neptune': 'Earth'}

    return (planets_1_dict[planet1], planets_2_dict[
