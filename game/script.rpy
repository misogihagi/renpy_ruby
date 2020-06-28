## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('鰐淵')

style ruby_style is default:
    size 12
    yoffset -20

style say_dialogue:
    line_leading 12
    ruby_style style.ruby_style

## The game starts here.

label start:
    
    scene image Frame("e1248_1.jpg", 2,2)
    show image "school_furyou_tsuppari.png"

    e "\"{rb}事故{/rb}{rt}ジコ{/rt}\"る奴{rt}ヤツ{/rt}は…\"{rb}不運{/rb}{rt}ハードラック{/rt}\"と踊{rt}ダンス{/rt}\"っちまったんだよ…"



    ## This ends the game.

    return
