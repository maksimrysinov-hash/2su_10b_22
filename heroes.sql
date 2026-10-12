CREATE TABLE heroes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    class VARCHAR(30) NOT NULL,
    level INT DEFAULT 1,
    hp INT NOT NULL,
    mp INT NOT NULL,
    attack INT NOT NULL,
    defence INT NOT NULL,
    speed INT DEFAULT 10
);
INSERT INTO heroes (name, class, level, hp, mp, attack, defence, speed) 
VALUES 
    ('Georgi', 'Troop', 5, 150, 30, 45, 35, 15),
    ('Petar', 'Mage', 5, 80, 80, 60, 15, 20);
SELECT * FROM heroes;
