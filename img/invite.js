const { MessageEmbed, Message } = require('discord.js');
const config = require('../config.json');

module.exports = {
	name: 'invite', 
	description: 'Me convide para seu servidor.',
    
	execute(message) {
		const { commands } = message.client;
        
        message.channel.send(
            new MessageEmbed()
            .setTitle(`${config.subtitulo} | Me convide`)
            .setDescription(`<:SUPPORT:1157392609933799444> **| Opa, para me convidar para seu servidor é nessario que você compre o bot, para ver a tabela de preços semanais e mensais do bot basta entrar em contato com aspect.cs**`)
            .setImage(config.banner)
            .setColor(config.color)
        );
	}
};