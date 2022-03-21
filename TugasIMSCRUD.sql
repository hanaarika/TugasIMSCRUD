/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.4.22-MariaDB : Database - pretestpraktikumims
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pretestpraktikumims` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `pretestpraktikumims`;

/*Table structure for table `tb_pertandingan` */

DROP TABLE IF EXISTS `tb_pertandingan`;

CREATE TABLE `tb_pertandingan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_peserta_a` int(11) DEFAULT NULL,
  `id_peserta_b` int(11) DEFAULT NULL,
  `hasil` int(11) DEFAULT NULL,
  `mulai` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `selesai` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_peserta_a` (`id_peserta_a`),
  KEY `id_peserta_b` (`id_peserta_b`),
  CONSTRAINT `tb_pertandingan_ibfk_1` FOREIGN KEY (`id_peserta_a`) REFERENCES `tb_peserta` (`id`),
  CONSTRAINT `tb_pertandingan_ibfk_2` FOREIGN KEY (`id_peserta_b`) REFERENCES `tb_peserta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pertandingan` */

insert  into `tb_pertandingan`(`id`,`id_peserta_a`,`id_peserta_b`,`hasil`,`mulai`,`selesai`) values 
(1,1,2,10,'2022-03-05 18:01:20','15:32:24'),
(3,2,3,12,'2022-03-05 18:02:19','15:55:12'),
(4,2,4,14,'2022-03-05 18:02:01','16:12:43'),
(5,3,4,15,'2022-03-05 18:02:40','17:12:00'),
(6,3,2,11,'2022-03-05 18:02:55','18:12:23');

/*Table structure for table `tb_peserta` */

DROP TABLE IF EXISTS `tb_peserta`;

CREATE TABLE `tb_peserta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_depan` varchar(255) DEFAULT NULL,
  `nama_belakang` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `no_telp` varchar(13) DEFAULT NULL,
  `id_rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_rank` (`id_rank`),
  CONSTRAINT `tb_peserta_ibfk_1` FOREIGN KEY (`id_rank`) REFERENCES `tb_rank` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_peserta` */

insert  into `tb_peserta`(`id`,`nama_depan`,`nama_belakang`,`alamat`,`no_telp`,`id_rank`) values 
(1,'Nadia','Azizah','Jl. West Life','082121837182',1),
(2,'Drew','Neros','Jl. Tukad Asih','0812173172',NULL),
(3,'Hana','Arika','Jl. Buana Asri','082172181',NULL),
(4,'Kurnia','Sari','Jl. Tukad Pakerisan','0821317232',NULL),
(5,'Nara','Arika','Jl. Tukad Buana','0821261631',NULL),
(7,'Dreq','Alchemy','Jl. Bumbak','081217381281',NULL);

/*Table structure for table `tb_rank` */

DROP TABLE IF EXISTS `tb_rank`;

CREATE TABLE `tb_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank` int(11) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_rank` */

insert  into `tb_rank`(`id`,`rank`,`deskripsi`) values 
(1,1,'Juara 1'),
(2,2,'Juara 2'),
(3,3,'Juara 3');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
