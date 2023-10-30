init:
    # 3066339771 код
    #===============================================
    # объявление мода
    $ mods['Steps'] = u'{color=#ff0000}Шаги{/color}'
    #===============================================
    
    # консоль разраба
    $ config.developer = True

    #===============================================
    # объявление персонажей
        #* гг
    $ gg = Character(name='Главный герой', what_color='#ffdd7d', color='#3ef511')
    #===============================================


    #===============================================
    # объявление спрайтов
        #* пионер в крови
    image pion = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( "Steps/Materials/Sprites/bloody_pioneer.png", im.matrix.tint(0.94, 0.82, 1.0) ),
        "persistent.sprite_time=='night'",im.MatrixColor( "Steps/Materials/Sprites/bloody_pioneer.png", im.matrix.tint(0.63, 0.78, 0.82) ),
        True, "Steps/Materials/Sprites/bloody_pioneer.png" )
        #* алиса в спортивке удивленная
    image dv sport surpr = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( "Steps/Materials/Sprites/Alice/dv_sport_surpeise.png", im.matrix.tint(0.94, 0.82, 1.0) ),
        "persistent.sprite_time=='night'",im.MatrixColor( "Steps/Materials/Sprites/Alice/dv_sport_surpeise.png", im.matrix.tint(0.63, 0.78, 0.82) ),
        True, "Steps/Materials/Sprites/Alice/dv_sport_surpeise.png" )
    image dv sport dream = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( "Steps/Materials/Sprites/Alice/dv_sport_dream.png", im.matrix.tint(0.94, 0.82, 1.0) ),
        "persistent.sprite_time=='night'",im.MatrixColor( "Steps/Materials/Sprites/Alice/dv_sport_dream.png", im.matrix.tint(0.63, 0.78, 0.82) ),
        True, "Steps/Materials/Sprites/Alice/dv_sport_dream.png" )
    #===============================================


    #===============================================
    # объявление музыки
        #* красная королева
    $ music_red_princess = 'Steps/Materials/Music/АлексейАйги-Красная Королева.mp3'
        #* из hotline maiami
    $ music_hotline_miami = 'Steps/Materials/Music/IAMTHEKIDYOUKNOWWHATIMEAN - Run.mp3'
        #* буерак
    $ music_buerak = 'Steps/Materials/Music/-_Remastered_music.mp3'
        #* алан хз
    $ music_alan = 'Steps/Materials/Music/The_Highlander_-_Emotional_Overload_Allan_McLoud_Club_Mix_cut_194sec.mp3'
    #===============================================


    #===============================================
    # объявление звуков
        #* нормальные шаги
    $ sfx_normal_steps = 'Steps/Materials/Sounds/medium_fast_steps.mp3'
        #* медленные шаги с эхо
    $ sfx_slow_steps = 'Steps/Materials/Sounds/shagi_s_effektom_eho.mp3'
    #===============================================


    #===============================================
    # объявление бг
        #* пустой домик
    image int_empty_house = 'Steps/Materials/BackGrounds/empty_house.jpg'
        #* чистая комната семена
    image int_semen_room = 'Steps/Materials/BackGrounds/int_semen_room_clean2.jpg'
    #===============================================


    #===============================================
    # объявление артов
        #* семен и алиса в катакомбах
    image cg_s_and_a_catacombs = 'Steps/Materials/Arts/s_and_a_catacombs.jpg'
    #===============================================






# начало мода
label Steps:
    jump main
