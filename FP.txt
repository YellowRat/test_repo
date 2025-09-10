Code

Article
Talk
Read
View source
View history

Tools
Page semi-protected
From Wikipedia, the free encyclopedia
For other uses, see Code (disambiguation). "Encoding" redirects here. For other uses, see Encoding (disambiguation).
For technical reasons, terms beginning with "Code#" redirect here. For the EPs by Ladies' Code, see Code 01 Bad Girl and Code 02 Pretty Pretty.

This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.
Find sources: "Code" – news · newspapers · books · scholar · JSTOR (March 2010) (Learn how and when to remove this template message)
In communications and information processing, code is a system of rules to convert information—such as a letter, word, sound, image, or gesture—into another form, sometimes shortened or secret, for communication through a communication channel or storage in a storage medium. An early example is an invention of language, which enabled a person, through speech, to communicate what they thought, saw, heard, or felt to others. But speech limits the range of communication to the distance a voice can carry and limits the audience to those present when the speech is uttered. The invention of writing, which converted spoken language into visual symbols, extended the range of communication across space and time.

The process of encoding converts information from a source into symbols for communication or storage. Decoding is the reverse process, converting code symbols back into a form that the recipient understands, such as English or/and Spanish.

One reason for coding is to enable communication in places where ordinary plain language, spoken or written, is difficult or impossible. For example, semaphore, where the configuration of flags held by a signaler or the arms of a semaphore tower encodes parts of the message, typically individual letters, and numbers. Another person standing a great distance away can interpret the flags and reproduce the words sent.

Theory
Main article: Coding theory
In information theory and computer science, a code is usually considered as an algorithm that uniquely represents symbols from some source alphabet, by encoded strings, which may be in some other target alphabet. An extension of the code for representing sequences of symbols over the source alphabet is obtained by concatenating the encoded strings.

Before giving a mathematically precise definition, this is a brief example. The mapping

�
=
{
�
↦
0
,
�
↦
01
,
�
↦
011
}
C = \{\, a\mapsto 0, b\mapsto 01, c\mapsto 011\,\}
is a code, whose source alphabet is the set 
{
�
,
�
,
�
}
\{a,b,c\} and whose target alphabet is the set 
{
0
,
1
}
\{0,1\}. Using the extension of the code, the encoded string 0011001 can be grouped into codewords as 0 011 0 01, and these in turn can be decoded to the sequence of source symbols acab.

Using terms from formal language theory, the precise mathematical definition of this concept is as follows: let S and T be two finite sets, called the source and target alphabets, respectively. A code 
�
:
�
→
�
∗C:\, S \to T^* is a total function mapping each symbol from S to a sequence of symbols over T. The extension 
�
′
C' of 
�
C, is a homomorphism of 
�
∗S^{*} into 
�
∗T^{*}, which naturally maps each sequence of source symbols to a sequence of target symbols.

Variable-length codes
Main article: Variable-length code
In this section, we consider codes that encode each source (clear text) character by a code word from some dictionary, and concatenation of such code words give us an encoded string. Variable-length codes are especially useful when clear text characters have different probabilities; see also entropy encoding.

A prefix code is a code with the "prefix property": there is no valid code word in the system that is a prefix (start) of any other valid code word in the set. Huffman coding is the most known algorithm for deriving prefix codes. Prefix codes are widely referred to as "Huffman codes" even when the code was not produced by a Huffman algorithm. Other examples of prefix codes are country calling codes, the country and publisher parts of ISBNs, and the Secondary Synchronization Codes used in the UMTS WCDMA 3G Wireless Standard.

Kraft's inequality characterizes the sets of codeword lengths that are possible in a prefix code. Virtually any uniquely decodable one-to-many code, not necessarily a prefix one, must satisfy Kraft's inequality.

Error-correcting codes
Main article: Error detection and correction
See also: Block code
Codes may also be used to represent data in a way more resistant to errors in transmission or storage. This so-called error-correcting code works by including carefully crafted redundancy with the stored (or transmitted) data. Examples include Hamming codes, Reed–Solomon, Reed–Muller, Walsh–Hadamard, Bose–Chaudhuri–Hochquenghem, Turbo, Golay, algebraic geometry codes, low-density parity-check codes, and space–time codes. Error detecting codes can be optimised to detect burst errors, or random errors.

Examples
Codes in communication used for brevity
Main article: Brevity code
A cable code replaces words (e.g. ship or invoice) with shorter words, allowing the same information to be sent with fewer characters, more quickly, and less expensively.

Codes can be used for brevity. When telegraph messages were the state of the art in rapid long-distance communication, elaborate systems of commercial codes that encoded complete phrases into single mouths (commonly five-minute groups) were developed, so that telegraphers became conversant with such "words" as BYOXO ("Are you trying to weasel out of our deal?"), LIOUY ("Why do you not answer my question?"), BMULD ("You're a skunk!"), or AYYLU ("Not clearly coded, repeat more clearly."). Code words were chosen for various reasons: length, pronounceability, etc. Meanings were chosen to fit perceived needs: commercial negotiations, military terms for military codes, diplomatic terms for diplomatic codes, any and all of the preceding for espionage codes. Codebooks and codebook publishers proliferated, including one run as a front for the American Black Chamber run by Herbert Yardley between the First and Second World Wars. The purpose of most of these codes was to save on cable costs. The use of data coding for data compression predates the computer era; an early example is the telegraph Morse code where more-frequently used characters have shorter representations. Techniques such as Huffman coding are now used by computer-based algorithms to compress large data files into a more compact form for storage or transmission.

Character encodings
Main article: Character encoding
Character encodings are representations of textual data. A given character encoding may be associated with a specific character set (the collection of characters which it can represent), though some character sets have multiple character encodings and vice versa. Character encodings may be broadly grouped according to the number of bytes required to represent a single character: there are single-byte encodings, multibyte (also called wide) encodings, and variable-width (also called variable-length) encodings. The earliest character encodings were single-byte, the best-known example of which is ASCII. ASCII remains in use today, for example in HTTP headers. However, single-byte encodings cannot model character sets with more than 256 characters. Scripts that require large character sets such as Chinese, Japanese and Korean must be represented with multibyte encodings. Early multibyte encodings were fixed-length, meaning that although each character was represented by more than one byte, all characters used the same number of bytes ("word length"), making them suitable for decoding with a lookup table. The final group, variable-width encodings, is a subset of multibyte encodings. These use more complex encoding and decoding logic to efficiently represent large character sets while keeping the representations of more commonly used characters shorter or maintaining backward compatibility properties. This group includes UTF-8, an encoding of the Unicode character set; UTF-8 is the most common encoding of text media on the Internet.

Genetic code
Main article: Genetic code
Biological organisms contain genetic material that is used to control their function and development. This is DNA, which contains units named genes from which messenger RNA is derived. This in turn produces proteins through a genetic code in which a series of triplets (codons) of four possible nucleotides can be translated into one of twenty possible amino acids. A sequence of codons results in a corresponding sequence of amino acids that form a protein molecule; a type of codon called a stop codon signals the end of the sequence.

Gödel code
In mathematics, a Gödel code was the basis for the proof of Gödel's incompleteness theorem. Here, the idea was to map mathematical notation to a natural number (using a Gödel numbering).

Other
There are codes using colors, like traffic lights, the color code employed to mark the nominal value of the electrical resistors or that of the trashcans devoted to specific types of garbage (paper, glass, organic, etc.).

In marketing, coupon codes can be used for a financial discount or rebate when purchasing a product from a (usual internet) retailer.

In military environments, specific sounds with the cornet are used for different uses: to mark some moments of the day, to command the infantry on the battlefield, etc.

Communication systems for sensory impairments, such as sign language for deaf people and braille for blind people, are based on movement or tactile codes.

Musical scores are the most common way to encode music.

Specific games have their own code systems to record the matches, e.g. chess notation.

Cryptography
In the history of cryptography, codes were once common for ensuring the confidentiality of communications, although ciphers are now used instead.

Secret codes intended to obscure the real messages, ranging from serious (mainly espionage in military, diplomacy, business, etc.) to trivial (romance, games) can be any kind of imaginative encoding: flowers, game cards, clothes, fans, hats, melodies, birds, etc., in which the sole requirement is the pre-agreement on the meaning by both the sender and the receiver.

Other examples
Other examples of encoding include:

Encoding (in cognition) - a basic perceptual process of interpreting incoming stimuli; technically speaking, it is a complex, multi-stage process of converting relatively objective sensory input (e.g., light, sound) into a subjectively meaningful experience.
A content format - a specific encoding format for converting a specific type of data to information.
Text encoding uses a markup language to tag the structure and other features of a text to facilitate processing by computers. (See also Text Encoding Initiative.)
Semantics encoding of formal language A informal language B is a method of representing all terms (e.g. programs or descriptions) of language A using language B.
Data compression transforms a signal into a code optimized for transmission or storage, generally done with a codec.
Neural encoding - the way in which information is represented in neurons.
Memory encoding - the process of converting sensations into memories.
Television encoding: NTSC, PAL and SECAM
Other examples of decoding include:

Decoding (computer science)
Decoding methods, methods in communication theory for decoding codewords sent over a noisy channel
Digital signal processing, the study of signals in a digital representation and the processing methods of these signals
Digital-to-analog converter, the use of analog circuit for decoding operations
Word decoding, the use of phonics to decipher print patterns and translate them into the sounds of language
Codes and acronyms
Acronyms and abbreviations can be considered codes, and in a sense, all languages and writing systems are codes for human thought.

International Air Transport Association airport codes are three-letter codes used to designate airports and used for bag tags. Station codes are similarly used on railways but are usually national, so the same code can be used for different stations if they are in different countries.

Occasionally, a code word achieves an independent existence (and meaning) while the original equivalent phrase is forgotten or at least no longer has the precise meaning attributed to the code word. For example, '30' was widely used in journalism to mean "end of story", and has been used in other contexts to signify "the end".[1] [2]

UML (англ. Unified Modeling Language) — уніфікована мова моделювання, використовується у парадигмі об'єктно-орієнтованого програмування. Є невід'ємною частиною уніфікованого процесу розробки програмного забезпечення. UML є мовою широкого профілю, це відкритий стандарт, що використовує графічні позначення для створення абстрактної моделі системи, яка називається UML-моделлю. UML був створений для визначення, візуалізації, проєктування й документування в основному програмних систем. UML не є мовою програмування, але в засобах виконання UML-моделей як інтерпретованого коду можлива кодогенерація.

Перша версія (1.0) UML вийшла 13 січня 1997, вона була створена консорціумом UML Partners за запитом Object Management Group (OMG) — організації, відповідальної за прийняття стандартів в галузі об'єктних технологій і баз даних. Після обговорення, у вересні 1997 року, версія 1.1 UML була представлена на голосування в OMG. Розробку UML підтримали і вже тоді використовували як стандарт такі гранди ринку інформаційних технологій, як Microsoft, IBM, Hewlett-Packard, Oracle, DEC, Sybase, Logic Works й інші.

Поточна версія — 2.0.


Зміст
1	Застосування
2	Історія створення
3	Діаграми
3.1	Структурні діаграми
3.1.1	Діаграма профілю
3.1.2	Діаграма класів
3.1.3	Діаграма компонентів
3.1.4	Діаграма композитної/складеної структури
3.1.5	Діаграма розгортання
3.1.6	Діаграма об'єктів
3.1.7	Діаграма пакетів
3.1.8	Діаграма станів (кінцевих автоматів)
3.1.9	Діаграма синхронізації
4	Призначення та рівні моделей
5	Метамоделювання
6	Представлення моделей
6.1	Представлення UML 1
6.1.1	Представлення використання
6.1.2	Представлення проектування
6.1.3	Представлення процесів
6.1.4	Представлення компонентів
6.1.5	Представлення розгортання
6.2	Представлення UML 2
6.2.1	Статичне представлення
6.2.2	Представлення проектування
6.2.3	Представлення використання
6.2.4	Представлення кінцевих автоматів
6.2.5	Представлення діяльності
6.2.6	Представлення взаємодії
6.2.7	Представлення розгортання
6.2.8	Представлення управління моделлю
7	Критика
8	Див. також
9	Примітки
10	Посилання
11	Література
Застосування
UML може бути застосовано на всіх етапах життєвого циклу аналізу бізнес-систем і розробки прикладних програм. Різні види діаграм які підтримуються UML, і найбагатший набір можливостей представлення певних аспектів системи робить UML універсальним засобом опису як програмних, так і ділових систем.

Діаграми дають можливість представити систему (як ділову, так і програмну) у такому вигляді, щоб її можна було легко перевести в програмний код.

Основною причиною використання мови UML є спілкування розробників між собою.[1]

Крім того, UML спеціально створювалася для оптимізації процесу розробки програмних систем, що дозволяє збільшити ефективність їх реалізації у кілька разів і помітно поліпшити якість кінцевого продукту.

UML чудово зарекомендувала себе в багатьох успішних програмних проєктах. Засоби автоматичної генерації кодів дозволяють перетворювати моделі мовою UML у вихідний код об'єктно-орієнтованих мов програмування, що ще більш прискорює процес розробки.

Практично усі CASE-засоби (програми автоматизації процесу аналізу і проєктування) мають підтримку UML. Моделі розроблені в UML, дозволяють значно спростити процес кодування і направити зусилля програмістів безпосередньо на реалізацію системи.

Діаграми підвищують супроводжуваність проєкту і полегшують розробку документації.

UML необхідний:

керівникам проєктів, які керують розподілом завдань і контролем за проєктом
проєктувальникам інформаційних систем які розробляють технічні завдання для програмістів;
бізнес-аналітикам, які досліджують реальну систему і здійснюють інжиніринг і реінжиніринг бізнесу компанії;
програмістам які реалізують модулі інформаційної системи.
При модифікації системи об'єктний підхід дозволяє легко включати в систему нові об'єкти і виключати застарілі без істотної зміни її життєздатності. Використання побудованої моделі при модифікаціях системи дає можливість усунути небажані наслідки змін, оскільки вони не ламають структури системи, а тільки змінюють поведінку об'єктів.

Історія створення
Починаючи із середини 60-х років і донедавна, широке поширення мали структурні методології аналізу, проєктування і розробки інформаційних систем, що характеризуються штучним поділом (часто неоптимальним) системи на підсистеми, а також слабким взаємозв'язком процесів і даних які присутні в системі. На відміну від них, об'єктні технології, орієнтовані на тісний взаємозв'язок процесів і даних у системах, дозволяють програмним системам бути надійнішими, легшими для реалізації і стійкішими до змін. Крім того, така філософія моделювання найбільше відповідає загальним концепціям поведінки систем реального світу.

Незважаючи на явну перевагу об'єктно-орієнтованих технологій аналізу і проєктування перед структурними, їхнє поширення було незначним, оскільки жоден з методів не давав єдиної і цілісної об'єктної моделі системи. Кожен метод добре висвітлював одну або декілька сторін реальної системи, залишаючи в тіні багато інших, не менш важливих сторін. Крім того, відсутність єдиного стандарту дуже заважало широкому поширенню об'єктно-орієнтованих методів при розробці програмного забезпечення.

Протягом 1994-96 років творці трьох найпоширеніших методологій — Граді Буч (BOOCH), Джим Рамбо (OMT — Object Modeling Technique) і Айвар Якобсон (OOSE — Object Oriented Software Engineering) об'єднали свої зусилля під егідою Rational Software Corporation для створення єдиної мови моделювання, яка б об'єднала всі істотні й успішні розробки в даній галузі і стала би стандартом мови об'єктного моделювання. Грандіозна робота, у якій поряд з Rational брали участь представники багатьох компаній, таких, як Microsoft, IBM, Hewlett-Packard, Oracle, DEC, Unisys, IntelliCorp, Platinum Technology і кількох сотень інших завершилася створенням у січні 1997 року UML 1.0, яка після бурхливого обговорення протягом 1997 року у вересні під версією 1.1 і була передана в OMG для прийняття як галузевий стандарт мови об'єктного моделювання.

Діаграми

Колаж з різних діаграм UML
В UML використовується 14 видів діаграм (для уникнення непорозумінь, також наведено англомовні назви):

Structure Diagrams:

Class diagram
Component diagram
Composite structure diagram
Collaboration (UML2.0)
Deployment diagram
Object diagram
Package diagram
Behavior Diagrams:

Activity diagram
State Machine diagram
Use case diagram
Interaction Diagrams:
Collaboration (UML1.x) /
Communication diagram (UML2.0)
Interaction overview diagram (UML2.0)
Sequence diagram
UML Timing Diagram (UML2.0)
Структурні діаграми:

Класів
Компонентів
Композитної/складеної структури
Кооперації (UML2.0)
Розгортування
Об'єктів
Пакетів
Діаграми поведінки:

Діяльності
Станів
Прецедентів
Діаграми взаємодії:

Кооперації (UML1.x) /
Комунікації (UML2.0)
Огляду взаємодії (UML2.0)
Послідовності
Синхронізації (UML2.0)
Uml diagram2

Структурні діаграми
Структурні діаграми (англ. Structure Diagrams) відображають статичні стани системи. За їхньою допомогою виділяються основні елементи системи, яка проектується. Оскільки структурні діаграми відображують саме структури, вони використовуються при документуванні архітектури програмного забезпечення.

Діаграма профілю
Діаграма профілю (англ. Profile Diagram) — діаграма профілю працює на рівні метамоделі, щоб показати стереотипи як класи зі стереотипом «стереотип», а профілі як пакети зі стереотипом «профіль». Відношення розширення (суцільна лінія із замкнутим, заповненим наконечником стрілки) вказує, який елемент метамоделі поширює даний стереотип. Діаграма профілю не існувала в UML 1. Вона була представлена в UML 2 для відображення використання профілів. До її впровадження для відображення цієї проблеми використовувалися інші діаграми.

Діаграма класів
Докладніше: Діаграма класів
Діаграма класів (англ. Class Diagram) — статична структурна діаграма, яка описує струкутру системи, демонструє класи системи, їхні атрибути, методи й залежності між класами.

Діаграма компонентів
Діаграма компонентів (англ. Component diagram) — статична структурна діаграма, яка показує поділ програмної системи на структурні компоненти й зв'язки (залежності) між компонентами. В якості фізичних компонентів можуть виступати файли, бібліотеки, модулі, файли виконання, пакети й т.п.

Діаграма композитної/складеної структури
Файл:Decorator template.png
Decorator template
Діаграма композитної/складеної структури (англ. Composite structure diagram) — статична структура діаграма, яка демонструє внутрішню структура класів й, за можливістю, взаємодію елементів (частин) внутрішньої структури класу.

Підвидом діаграм композитної структури є діаграми кооперації (англ. Collaboration diagram, введені в UML 2.0), які показують ролі й взаємодію класів у рамках кооперації. Кооперації є зручними для моделювання шаблонів проектування.

Діаграми композитної структури можуть використовуватися разом з діаграмами класів.

Діаграма розгортання
Діаграма розгортання, діаграма розміщення (англ. Deployment diagram) — слугує для моделювання працюючих вузлів (апаратних засобів, англ. node) й артефактів, які на них розгорнуті. У UML2 на вузлах розгортаються артефакти, (англ. artifact), тоді як у UML1 на вузлах розгоралися компоненти. Між артефактом і логічним елементом (компонентом), який він реалізує, установлюється залежність маніфестації.

Діаграма об'єктів
Діаграма об'єктів (англ. Object diagram) — демонструє повний або частковий знімок системи, яка моделюється, у заданий момент часу. На діаграмі об'єктів відображуються примірники класів (об'єкти) системи з указанням поточних значень їхніх атрибутів й зв'язків між об'єктами.

Діаграма пакетів
Діаграма пакетів (англ. Package diagram) — структуран діаграма, основним змістом якої є пакети і відношення між ними. Жорсткий розділ між різними структурними діаграмами не проводиться, тому дана назва пропонується виключно для зручності й не має семантичного значення (пакети й діаграми пакетів можуть бути присутніми на інших структурних діаграмах). Діаграми пакетів служать, насамперед, в організацію елементів у групи за ознакою з метою спрощення структури та організації роботи з моделлю системи.

Діаграма станів (кінцевих автоматів)
Докладніше: Діаграма станів (UML)
Діаграма синхронізації
Докладніше: Діаграма синхронізації (UML)
Призначення та рівні моделей
Залежно від цілей використання моделі можуть бути таких основних рівнів:

концептуальна модель, модель аналізу (англ. conceptual model) — модель предметної області, у ній присутні тільки класи прикладних об'єктів, використовується для управління процесом мислення, розуміння; потребує концептуальної цілісності (англ. consistency);
модель проектування (англ. design model) — високороівневий (на рівні підсистем) та низькорівневий (на рівні класів) опис програмної сисеми; на її основі розробляється програмний код застосунку; призначена для подальшої розробки моделей реалізації; головна вимога — зрозумілість (англ. usability).
модель реалізації (англ. implementation model) — призначена для автоматичного перетворення в інший вид, наприклад, у програмний код, який виконується; (при використанні об'єктно-орієнтованих мов програмування); головна вимога — повнота (англ. completeness).
Метамоделювання

Ілюстрація Meta-Object Facility
Object Management Group (OMG) розробила архітектуру метамоделювання для визначення UML, яка називається Meta-Object Facility (MOF).[2] MOF розроблена як чотиришарова архітектура, як показано на зображенні праворуч. Вона забезпечує мета-мета-модель у верхній частині, яка називається шаром M3. Ця M3-модель є мовою, що використовується Meta-Object Facility для побудови метамоделей, які називаються M2-моделями.

Найяскравішим прикладом мета-об'єктної моделі 2-го рівня є метамодель UML, яка описує саму мову UML. Ці M2-моделі описують елементи M1-рівня, а отже, і M1-моделі. Це можуть бути, наприклад, моделі, написані на UML. Останній рівень - це M0-рівень або рівень даних. Він використовується для опису екземплярів системи під час виконання.[3]

Мета-модель може бути розширена за допомогою механізму, який називається стереотипізацією. Він був підданий критиці як недостатній/неприйнятний Брайаном Хендерсоном-Селлерсом та Сезаром Гонсалесом-Пересом у статті "Використання та зловживання механізмом стереотипів в UML 1.x та 2.0".[4]

Представлення моделей

Представлення з UML 1
Представлення UML 1
Представлення використання
Представлення використання (англ. Use Case View) — опис поведінки системи з точки зору зовнішніх дійових осіб, опис її функціональних вимог. Структурні аспекти відображуються за допомогою діаграм варіантів використання, а поведінкові — за допомогою діаграмам взаємодії, стану і діяльності.

Представлення проектування
Представлення проектування (англ. Design View) — призначене для опису словника предметної області, тобто класів, а також допоміжних сутностей, таких як інтерфейси та кооперації. Структурні аспекти передаються діаграмами класів і об'єктів, а поведінкові — діаграмами взаємодії, стану і діяльності.

Представлення процесів
Представлення процесів (англ. Process view) — опис взаємодії елементів управління (процесів, потоків) під час роботи системи. Структурні аспекти передаються за допомогою концепції активних класів, які представляють процеси і потоки, а поведінкові аспекти — діаграмами взаємодії, стану і діяльності.

Представлення компонентів
Представлення компонентів (англ. Component view) — опис системи на рівні артефактів (компонентів, файлів і т.д.), які використовуються для збирання, випуску, конфігурації програмного продукту. Структурні аспекти передаються діаграмами компонентів, а поведінкові аспекти — діаграмами взаємодії, стану і діяльності.

Представлення розгортання
Представлення розгортання (англ. Deployment view) — відображення топології зв'язків апаратних засобів і розміщення на них компонентів. Структурні аспекти передаються діаграмами розгортання, а поведінкові аспекти — діаграмами взаємодії, стану і діяльності.

Представлення UML 2
Статичне представлення
Статичне представлення (англ. Static view) — відображення статичної структури системи без опису динаміки у будь-якому прояві. Як правило, статичне представлення відображує логічні концепції програмного забезпечення, основою якого є класи і їх відносини.

Діаграми, які використовуються для статичного представлення: діаграма класів.

Представлення проектування
Представлення проектування (англ. Design view) — більш деталізований варіант статичного представлення, з виділенням класифікацій, які забезпечують необхідну функціональність системи.

Діаграми, які використовуються для представлення проектування: діаграма внутрішньої структури, діаграма комунікації, діаграма компонентів.

Представлення використання
Представлення використання (англ. Use Case view) — опис функціонування системи у термінах варіантів використання і розглядає їх з точки зору зацікавлених дійових осіб.

Діаграми, які використовуються для представлення використання: діаграма використання (діаграма прецедентів).

Представлення кінцевих автоматів
Представлення кінцевих автоматів (англ. State machine view) — відображує поведінку окремих елементів, до яких можна застосувати поняття життєвого циклу, який описується набором станів і переходів між ними.

Діаграми, які використовуються для представлення кінцевих автоматів: діаграма кінцевих автоматів (діграма станів).

Представлення діяльності
Представлення діяльності (англ. Activity view) — опис системи з точки зору різних елементів діяльності, які поєднані потоками управління і потоками даних.

Діаграми, які використовуються для представлення діяльності: діаграма діяльності, оглядова діаграма взаємодії.

Представлення взаємодії
Представлення взаємодії (англ. Interaction view) — відображення послідовності обміну повідомленнями між елементами системи під час виконання додатку.

Діаграми, які використовуються для представлення взаємодії: діаграма послідовності, діаграма комунікації, діаграма синхронізації.

Представлення розгортання
Представлення управління моделлю
Критика
Попри те, що UML є широко визнаним стандартом мови моделювання, вона часто підпадає під критику через такі причини:

Надмірність мови
Неточна семантика
Проблеми у вивченні та застосуванні
Візуальна неоднорідність
Намагається подобатись усім

Robert Aragon	489-36-8350	4929-3813-3266-4295
Ashley Borden	514-14-8905	5370-4638-8881-3020
Thomas Conley	690-05-5315	4916-4811-5814-8111
Susan Davis	421-37-1396	4916-4034-9269-8783Robert Aragon	489-36-8350	4929-3813-3266-4295
Ashley Borden	514-14-8905	5370-4638-8881-3020
Thomas Conley	690-05-5315	4916-4811-5814-8111
Susan Davis	421-37-1396	4916-4034-9269-8783

Хаширама Сенджу (1 хокаґе)
Тобірама Сенджу (2 хокаґе)
Хірузен Сарутобі (3 хокаґе)
Намікадзе Мінато (4 хокаґе)
Цунаде Сенджу (5 хокаґе)
Хатаке Какаші (6 хокаґе)
Удзумакі Наруто (7 хокаґе)
Суна (Казекаґе)
Рето (1 казекаґе)
Шамон (2 казекаґе)
ім'я невідоме (3 казекаґе)
Раса (4 казекаґе)
Ґаара (5 казекаґе)
Кірі (Мідзукаґе)
Б'якурен (1 мідзукаґе)
Генгецу Хозукі (2 мідзукаґе)
ім'я невідоме (3 мідзукаґе)

Demesne far hearted suppose venture excited see had has. Dependent on so extremely delivered by. Yet no jokes worse her why. Bed one supposing breakfast day fulfilled off depending questions. Whatever boy her exertion his extended. Ecstatic followed handsome drawings entirely mrs one yet outweigh. Of acceptance insipidity remarkably is invitation.

Moments its musical age explain. But extremity sex now education concluded earnestly her continual. Oh furniture acuteness suspected continual ye something frankness. Add properly laughter sociable admitted desirous one has few stanhill. Opinion regular in perhaps another enjoyed no engaged he at. It conveying he continual ye suspected as necessary. Separate met packages shy for kindness.

Excited him now natural saw passage offices you minuter. At by asked being court hopes. Farther so friends am to detract. Forbade concern do private be. Offending residence but men engrossed shy. Pretend am earnest offered arrived company so on. Felicity informed yet had admitted strictly how you.

Entire any had depend and figure winter. Change stairs and men likely wisdom new happen piqued six. Now taken him timed sex world get. Enjoyed married an feeling delight pursuit as offered. As admire roused length likely played pretty to no. Means had joy miles her merry solid order.


Robert Aragon
489-36-8350
4929-3813-3266-4295
Ashley Borden
514-14-8905
5370-4638-8881-3020
Thomas Conley
690-05-5315
4916-4811-5814-8111
Susan Davis
421-37-1396
4916-4034-9269-8783
