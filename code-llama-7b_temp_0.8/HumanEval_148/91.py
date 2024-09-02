
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
    # code here
    # 建立圓環陣列
    # 根據圓環距離與轉換成小寫字串比較位置
    # 找出所有圓環位置在中間的位置
    # 根據圓環位置內的陣列位置來做判斷
    # 輸出圓環位置大小的陣列
    
    planets = [
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
    ]
    # 圓環位置
    planets_orbit = [
        0, 0.387, 0.723, 1.524, 5.203, 9.539, 19.191, 30.069, 39.481
    ]

    planets_orbit_lowercase = [i.lower() for i in planets]
    # print(planets_orbit_lowercase)

    # 將輸入的圓環名稱轉換成小寫字串
    planet1_lowercase = planet1.lower()
    planet2_lowercase = planet2.lower()

    # 判斷輸入是否是圓環名稱
    if planet1_lowercase in planets_orbit_lowercase and planet2_lowercase in planets_orbit_lowercase:
        # 將輸入的圓環名稱轉換成圓環位置
        planet1_index = planets_orbit_lowercase.index(planet1_lowercase)
        planet2_index
