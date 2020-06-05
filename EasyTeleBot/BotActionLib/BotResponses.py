from ..BotActionLib import ActionType
from ..BotActionLib.BotActionClass import BotAction
from ..GenericFunctions import GetFormatNames, Object, RemoveFormatName, RemoveUnreachableFormats


class TextResponse(BotAction):
    def PerformAction(self, bot, chat, message):
        text_response_format = self.data
        text_response_format = RemoveUnreachableFormats(text_response_format, chat)
        text_response = text_response_format.format(data=chat.data)
        if text_response == "":
            print("error - act id {} tried sending an empty text".format(self.id))
        else:
            bot.sendMessage(chat_id=chat.id, text=text_response,
                            reply_to_message_id=message.message_id, reply_markup=self.markup)
        return super(TextResponse, self).PerformAction(bot, chat, message)

    pass


class AnimationResponse(BotAction):
    def PerformAction(self, bot, chat, message):
        url_format = self.data
        url_format = RemoveUnreachableFormats(url_format, chat)
        url = url_format.format(data=chat.data)
        if url == "":
            print("act id {} tried sending an empty url animation".format(self.id))
        else:
            bot.sendAnimation(chat_id=chat.id, animation=url,
                              reply_to_message_id=message.message_id, reply_markup=self.markup)
        return super(AnimationResponse, self).PerformAction(bot, chat, message)


class PhotoResponse(BotAction):
    def PerformAction(self, bot, chat, message):
        return super(PhotoResponse, self).PerformAction(bot, chat, message)
        pass

    pass


ResponseTypeReferenceDictionary = {
    ActionType.TextResponse: TextResponse,
    ActionType.AnimationResponse: AnimationResponse,
}
