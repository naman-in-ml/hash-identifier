## In version 0.1
* take input form the user 
* store it as variable 
* count the lenght of the hash strings


###  Version 0.2 ( Now using if else ) 

* if length is 32 then MD5
* if length is 40 then SHA-1
* if length is 64 then SHA-256
* if length is 128 then SHa-512
* else unknow 

### Problems
* if there is 32 character then output will be md5 but it may not be hex for example **naman@@@@@@@@@@@@@@@@**
* so now i have to check each character of the strings it should be hex (0-9,a-z,A-Z) 

### Solution 

* just think about how you manually do 
 1. Make a list of valid characters
 2. Check each character
 3. If match → continue
 4. Else → invalid

 ### Version 0.3
 * using if `char in valid_chars` and `for char in hash_value` i can be sure that the string is hex 
 "Now i have to move this block after analysing lenght and before printing this is likely to be ...."

### Problems
* now if the lenght is 63 still it goes and chech each char 
* i want it to follow this strict scheme 
1. count the length if it is 32,40,64,128 only then it should check each char other wise print invalid string

### Soution 
IF length valid
    IF chars valid
        identify
    ELSE
        invalid chars
ELSE
    invalid length

































### Lessons Learned 
*  Remember that `Shift + Enter` in VS Code opens the interactive window. Use `exit()` to close it!
* i dont' understand properly how the identation works inside loops of if else 
* identation me problem ho rahi hai (bahut zyda hi problem ho gyi isme to )