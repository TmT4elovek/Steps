label good_end:
    window show dissolve

    'Я решил разбудить Алису, вместе можно было хоть что-то придумать.'

    stop sound_loop
    play sound_loop sfx_normal_steps volume 6.0

    ggzs_gg 'Алиса, Алиса, вставай!'
    'Она не просыпалась, на моё тряску её тела реакции не последовало. Шаги всё ближе. Ближе, ближе... Совсем рядом.'
    ggzs_gg 'Алиса, прошу вставай!'
    'Они уже на подходе, мои руки безумно трясутся, всё ещё пытаюсь разбудить Алису.'
    ggzs_gg 'ВСТАВАЙ!'

    scene bg white
    scene bg int_semen_room
    show dv sport_surprised
    with flash
    stop sound_loop
    stop sound_loop2
    stop music
    play music music_alan fadein 3


    ggzs_gg 'ВСТАВАЙ, ПРОШУ ВСТАВАЙ!'
    dv 'Ты чего разорался-то? Отпуск дали, так свою девушку будить можно?'
    'Я оцепенел.'
    'Что?...'
    dv 'Эй? Что такое?'
    'Выйдя из ступора, я осмотрелся по сторонам. Наша квартира, кровать, вон мой стол с компьютером.'
    ggzs_gg 'Что... Это было?'
    'Включив взятый с тумбы мобильник, у меня пропал дар речи.'
    '3:33, Понедельник, 21 число.'
    'Алиса встала с кровати и удивлённо посмотрела на меня.'
    'Мобильник выпал из рук. Меня осенило.'
    'Сон... Просто сон. Кошмар, самый обыкновенный кошмар. Они сняться каждому, у них бывают самые разные сюжеты и повороты событий.'
    'Эта информация была из недавно прочитанной мною статье по Википедии.'
    'Я расхохотался.'
    ggzs_gg 'Сон! Просто сон! Кошмар! Да и пошёл он к чёрту!'
    'Секунда и обнимаю Алису со всей силы, чуть ли не плача от моего пережитого страха.'
    dv 'Я понимаю конечно, я тебя люблю, ты меня любишь, я же всё-равно сильнее.'
    'Она ехидно улыбнулась.'
    ggzs_gg 'Ты не поверишь!'

    show dv sport_dream with dspr

    'Я улыбнулся в ответ и поцеловал её в губы. Нежно, настолько нежно, что я и начал забывать про ситуацию, в которой мне удалось недавно побывать.'
    'Сев рядом, я рассказал ей про своё сновидение. В деталях, описывая каждое моё чувство и движение.'
    'Её эмоции во время моего рассказала надо было видеть.'

    show dv sport_surprised with dspr

    dv 'Ничего себе...'
    dv 'И я там была?'
    'Удивлённо спросила она.'
    ggzs_gg 'Была. И я был. И даже пионер какой-то.'

    show dv sport_dream with dspr
    
    dv 'Да уж.'
    'Зевнула она и посмотрела на меня.'
    dv 'Тебе бы успокоительного выпить.'
    'Обеспокоенно сказала она.'
    ggzs_gg 'Да ладно, обойдусь уж.'

    scene black with dissolve
    window hide dissolve
    $ set_mode_nvl()
    nvl show dissolve

    'Мы легли на кровать. Спустя какое-то время Алиса засопела, прямо как в моём сне. И, видимо машинально, положила руку на мою грудь, этим самым обнимая меня.'
    'Спустя какое-то время уснул и я. Сон по-началу не шёл, в голове крутились мысли о лагере, катакомбах, загадочном пионере. На лбу выступил пот, стало страшно от мысли, что я сейчас усну и проснусь в этом комнате, а к нам приближаются шаги.'
    'Но спустя какое-то время, с чувством эйфории и полного спокойствия, в сон в пал и я. Грубоко в голове промелькнула мысль, что на работе мне дали отпуск, и ближайшие три недели, я смогу провести с Алисой.'

    nvl hide dissolve
    $ renpy.pause(2)
    return