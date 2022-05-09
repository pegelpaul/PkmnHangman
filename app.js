import { words } from "./monList/mons";
import { normal,ground,dragon,ice,elektrik,fairy,fire,flying,ghost,rock,poison,bug,fighting,grass,psychic,steel,dark,water } from "./monTypes/types";


// variables
const streak = 0;
const type = "null";

getValidWord = function () {
    const random = Math.floor(Math.random() * words.length)
    let word = words[random] 
    if (word in normal){
        type = 'Normal'
    } else if (word in ground) {
        type = 'Boden'
    } else if (word in dragon) {
        type = 'Drache'
    } else if (word in ice) {
        type = 'Eis'
    } else if (word in elektrik) {
        type = 'Elektro'
    } else if (word in fairy) {
        type = 'Fee'
    } else if (word in fire) {
        type = 'Feuer'
    } else if (word in flying) {
        type = 'Flug'
    } else if (word in ghost) {
        type = 'Geist'
    } else if (word in rock) {
        type = 'Gestein'
    } else if (word in poison) {
        type = 'Gift'
    } else if (word in bug) {
        type = 'Käfer'
    } else if (word in fighting) {
        type = 'Kampf'
    } else if (word in grass) {
        type = 'Pflanze'
    } else if (word in psychic) {
        type = 'Psycho'
    } else if (word in steel) {
        type = 'Stahl'
    } else if (word in dark) {
        type = 'Unlicht'
    } else if (word in water) {
        type = 'Wasser'
    }
    return toUpperCase(word)
}

tryAgain = function() {
    // function to either close or play again (y/n)?
}

hangman = function () {
    let word = getValidWord();
    let wordLetters =  Set(word);
    let usedLetters = Set();
    let lives = 7;

    while (wordLetters.length > 0, lives > 0) {
        
    }

}