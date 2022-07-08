# ET has two classes - ElementTree (entire XML as a tree) and Element (single node in the tree)
import xml.etree.ElementTree as xml


class Beat:
    def __init__(self, name, bass, hihat, snare, clap, melody, chords):
        self.name = name
        self.bass = bass
        self.hihat = hihat
        self.snare = snare
        self.clap = clap
        self.melody = melody
        self.chords = chords

    def create_xml(self):
        root = xml.Element('Beats')

        b1 = xml.Element(self.name)
        root.append(b1)

        type1 = xml.SubElement(b1, 'bass')
        type1.text = self.bass

        type2 = xml.SubElement(b1, 'hihat')
        type2.text = self.hihat

        type3 = xml.SubElement(b1, 'snare')
        type3.text = self.snare

        type4 = xml.SubElement(b1, 'clap')
        type4.text = self.clap

        type5 = xml.SubElement(b1, 'melody')
        type5.text = self.melody

        type6 = xml.SubElement(b1, 'chords')
        type6.text = self.chords

        tree = xml.ElementTree(root)
        with open('beats.xml', 'wb') as files:
            tree.write(files)


def main():
    print('Enter name: ')
    name = input()
    print('Enter bass: ')
    bass = input()
    print('Enter hihat: ')
    hihat = input()
    print('Enter snare: ')
    snare = input()
    print('Enter clap: ')
    clap = input()
    print('Enter melody: ')
    melody = input()
    print('Enter chords: ')
    chords = input()
    beat = Beat(name, bass, hihat, snare, clap, melody, chords)
    beat.create_xml()


if __name__ == '__main__':
    main()
