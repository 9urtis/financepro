from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    print("Start function called")  # Pour le débogage
    keyboard = [
        [InlineKeyboardButton("Abonnement mensuel (20€)", callback_data='mensuel')],
        [InlineKeyboardButton("Abonnement annuel (200€)", callback_data='annuel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    response_message = "Bienvenue ! Je propose un programme d'analyses fondamentales approfondies et je partage mes positions. Pour vous abonner, veuillez choisir une option ci-dessous :"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message, reply_markup=reply_markup)

def subscription(update: Update, context: CallbackContext) -> None:
    print("Subscription function called")  # Pour le débogage
    query = update.callback_query
    query.answer()
    text = query.data
    paypal_link_mensuel = "https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-10U94726HF780193PMSLIV7I"
    stripe_link_mensuel = "https://buy.stripe.com/8wMcN60pg5j6bde8wx"
    stripe_link_annuel = "https://buy.stripe.com/4gw9AU2xo12Q2GI288"
    if text.lower() == "mensuel":
        keyboard = [
            [InlineKeyboardButton("Carte bancaire", url=stripe_link_mensuel),
            InlineKeyboardButton("Paypal", url=paypal_link_mensuel)],
            [InlineKeyboardButton("Contact Support", url="https://t.me/c9rtis")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        response_message = "Parfait ! Pour votre abonnement mensuel de 20€, facturé tous les 1 mois de manière récurrente, veuillez effectuer votre paiement via les liens suivants. Après le paiement, veuillez envoyer une preuve de paiement à notre support en cliquant sur 'Contact Support' pour être intégré au groupe."
        query.edit_message_text(text=response_message, reply_markup=reply_markup)
    elif text.lower() == "annuel":
        keyboard = [
            [InlineKeyboardButton("Carte bancaire", url=stripe_link_annuel)],
            [InlineKeyboardButton("Contact Support", url="https://t.me/c9rtis")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        response_message = "Parfait ! Pour votre abonnement annuel de 200€, facturé tous les 12 mois de manière récurrente, veuillez effectuer votre paiement via les liens suivants. Note: Le paiement via Paypal sera disponible prochainement. Après le paiement, veuillez envoyer une preuve de paiement à notre support en cliquant sur 'Contact Support' pour être intégré au groupe."
        query.edit_message_text(text=response_message, reply_markup=reply_markup)

def main():
    print("Main function called")  # Pour le débogage
    updater = Updater(token='6185343795:AAHD6qqKtdBybMXPGEaMG5Jn0FpQoumbG3U', use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    button_handler = CallbackQueryHandler(subscription)
    dp.add_handler(start_handler)
    dp.add_handler(button_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()
