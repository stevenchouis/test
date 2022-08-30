# 直接import package, 它會去import該目錄下的__init__.py
# 再使用該Package的__init__.py中所define的class
from telnetlib import STATUS
import package1 as pkg1

human1 = pkg1.Human("Steven", "male", "Taiwanese")
human1.speak("Taiwanese")
human1.speak("English")