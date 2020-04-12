# Ask1CV
First exercise of the project in Computer Vision concerning tresholding of an image.

Σχολιασμός αποτελέσματος πρώτης άσκησης:

Μετά από εναλλαγές τιμών του ορίου κατωφλίωσης για την εισαγώμενη εικόνα "trikoupi6.png" στο διάστημα τιμών [0,255] , παρατήρησα οτι όσο πιο μεγάλη ήταν η τιμή του ορίου κατωφλίωσης, τόσο πιο σκούρα ήταν η output εικόνα και πιο έντονες οι σκιάσεις της, συνεπώς το αποτέλεσμα δεν ήταν τόσο ευδιάκριτο. Αντιθέτως, όσο πιο μικρή τιμή έβαζα στο όριο κατωφλίωσης, τόσο πιο φωτεινή ήταν κ εξαφανιζόντουσαν οι μαύρες σκιάσεις και, κατά συνέπεια, ήταν πιο καθαρη η εικόνα. Μέχρι που έφτασα στην τιμή 35  και πλέον η εξαγώμενη εικόνα είχε ένα καθαρό λευκό φόντο και μαύρο το περιχόμενο ενδιαφέροντος ( στη περίπτωσή της εικόνας μας το κείμενο ). Αν συνέχιζα να μειώνω την τιμή, όμως, η εικόνα αρχιζε να υπερφωτίζεται και το μαύρο στοιχείο της θα ξεθώριαζε και θα υπερτερούσε το λευκό στοιχείο πλέον, γεγονός που δεν θα ήταν το επιθυμητό αποτέλεσμα.

Στο repository υπάρχουν τα εξής αρχεία:
  -το αρχείο ask1.py , που είναι το αρχείο με τον κώδικα του προγράμματος. Για να τρέξει στο τερματικό χρειάζεται 3 arguments,    το path της εισαγώμενης εικόνας, ένα όνομα για την εξαγώμενη εικόνα και μια τιμή για το όριο κατωφλίωσης που επιθυμώ να        εφαρμοστεί.
  
  -το αρχείο ask1.ipynd, το οποίο είναι το jupyter notbook αρχείο. Σε αυτό, δοκιμάζονται 5 διαφορετικές τιμές ορίου             κατωφλίωσης με το αντίστοιχο output για την κάθε μια. Ενδεχομένως το μόνο που θα χρειαστέι είναι να εισαχθεί το αντίστοιχο     path για την εικόνα που επιθυμούμε στη μεταβλητή inputImage.
