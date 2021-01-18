import requests
import random
import json
import plotly
import plotly.graph_objs as go
import datetime

city = str(input())

try:
    d = {21949: 'Забайкальский край', 1: 'Московская область', 2: 'Санкт-Петербург', 84: 'США', 93: 'Аргентина',
         94: 'Бразилия', 95: 'Канада', 96: 'Германия', 102: 'Великобритания', 113: 'Австрия', 114: 'Бельгия',
         115: 'Болгария', 116: 'Венгрия', 117: 'Литва', 118: 'Нидерланды', 119: 'Норвегия', 120: 'Польша',
         121: 'Словакия', 122: 'Словения', 123: 'Финляндия', 124: 'Франция', 125: 'Чехия', 126: 'Швейцария',
         127: 'Швеция', 134: 'Китай', 135: 'Южная Корея', 137: 'Япония', 139: 'Новая Зеландия', 149: 'Беларусь',
         159: 'Казахстан', 167: 'Азербайджан', 168: 'Армения', 169: 'Грузия', 171: 'Узбекистан', 179: 'Эстония',
         180: 'Сербия', 181: 'Израиль', 187: 'Украина', 203: 'Дания', 204: 'Испания', 205: 'Италия', 206: 'Латвия',
         207: 'Киргизия', 208: 'Молдавия', 209: 'Таджикистан', 210: 'ОАЭ', 211: 'Австралия', 213: 'Москва',
         225: 'Россия', 246: 'Греция', 959: 'Севастополь', 977: 'Республика Крым', 983: 'Турция', 994: 'Индия',
         995: 'Таиланд', 1056: 'Египет', 10000: 'Мир', 10013: 'Ямайка', 10015: 'Боливия', 10017: 'Куба',
         10020: 'Марокко', 10021: 'ЮАР', 10022: 'Сейшельские острова', 10023: 'Ливия', 10024: 'Тунис', 10030: 'Фиджи',
         10054: 'Албания', 10057: 'Босния и Герцеговина', 10063: 'Ирландия', 10064: 'Исландия', 10067: 'Лихтенштейн',
         10068: 'Северная Македония', 10069: 'Мальта', 10070: 'Монако', 10074: 'Португалия', 10077: 'Румыния',
         10083: 'Хорватия', 10088: 'Андорра', 10090: 'Афганистан', 10091: 'Бангладеш', 10093: 'Вьетнам',
         10095: 'Индонезия', 10097: 'Малайзия', 10098: 'Мальдивы', 10099: 'Монголия', 10101: 'Непал', 10102: 'Пакистан',
         10105: 'Сингапур', 10108: 'Филиппины', 10109: 'Шри-Ланка', 10174: 'Ленинградская область',
         10176: 'Ненецкий автономный округ', 10231: 'Республика Алтай', 10233: 'Республика Тыва',
         10243: 'Еврейская автономная область', 10251: 'Чукотский автономный округ', 10532: 'Бахрейн',
         10535: 'Иордания', 10536: 'Иран', 10537: 'Кувейт', 10538: 'Ливан', 10540: 'Саудовская Аравия', 10542: 'Сирия',
         10645: 'Белгородская область', 10650: 'Брянская область', 10658: 'Владимирская область',
         10672: 'Воронежская область', 10687: 'Ивановская область', 10693: 'Калужская область',
         10699: 'Костромская область', 10705: 'Курская область', 10712: 'Липецкая область', 10772: 'Орловская область',
         10776: 'Рязанская область', 10795: 'Смоленская область', 10802: 'Тамбовская область',
         10819: 'Тверская область', 10832: 'Тульская область', 10841: 'Ярославская область',
         10842: 'Архангельская область', 10853: 'Вологодская область', 10857: 'Калининградская область',
         10897: 'Мурманская область', 10904: 'Новгородская область', 10926: 'Псковская область',
         10933: 'Республика Карелия', 10939: 'Республика Коми', 10946: 'Астраханская область',
         10950: 'Волгоградская область', 10995: 'Краснодарский край', 11004: 'Республика Адыгея',
         11010: 'Республика Дагестан', 11012: 'Республика Ингушетия', 11013: 'Кабардино-Балкарская Республика',
         11015: 'Республика Калмыкия', 11020: 'Карачаево-Черкесская Республика',
         11021: 'Республика Северная Осетия — Алания', 11024: 'Чеченская Республика', 11029: 'Ростовская область',
         11069: 'Ставропольский край', 11070: 'Кировская область', 11077: 'Республика Марий Эл',
         11079: 'Нижегородская область', 11084: 'Оренбургская область', 11095: 'Пензенская область',
         11108: 'Пермский край', 11111: 'Республика Башкортостан', 11117: 'Республика Мордовия',
         11119: 'Республика Татарстан', 11131: 'Самарская область', 11146: 'Саратовская область',
         11148: 'Удмуртская Республика', 11153: 'Ульяновская область', 11156: 'Чувашская Республика',
         11158: 'Курганская область', 11162: 'Свердловская область', 11176: 'Тюменская область',
         11193: 'Ханты-Мансийский автономный округ — Югра', 11225: 'Челябинская область',
         11232: 'Ямало-Ненецкий автономный округ', 11235: 'Алтайский край', 11266: 'Иркутская область',
         11282: 'Кемеровская область', 11309: 'Красноярский край', 11316: 'Новосибирская область',
         11318: 'Омская область', 11330: 'Республика Бурятия', 11340: 'Республика Хакасия', 11353: 'Томская область',
         11375: 'Амурская область', 11398: 'Камчатский край', 11403: 'Магаданская область', 11409: 'Приморский край',
         11443: 'Республика Саха (Якутия)', 11450: 'Сахалинская область', 11457: 'Хабаровский край'}
    n_d = {v: k for k, v in d.items()}

    country = 'Россия'
    r = requests.get(
        'https://yastat.net/s3/milab/2020/covid19-stat/data/v5/data-by-region/{}.json?v=1608969856500'.format(city))

    data = json.loads(r.text)
    today_sl = data['cases'][-1][1]
    today_dead = data['deaths'][-1][1]
    today_dead_a = 'Число скончавшихся — ' + str(today_dead)

    if today_dead == 0:
        today_dead_a = 'Жертв вируса нет'

    viyavleno = 'о'
    novix = "х"
    cluchaev = "ев"

    if str(today_sl)[-1] == '1':
        viyavleno = ''
        novix = "й"
        cluchaev = "й"

    total_reg_sl = data['cases'][-1][0]
    total_reg_dead = data['deaths'][-1][0]

    stalo = 'о'
    if str(total_reg_dead)[-1] == '0':
        stalo = ''
    cheloveka = ''
    if str(total_reg_dead)[-1] in ['2', '3', '4']:
        cheloveka = 'а'

    r2 = requests.get(
        'https://yastat.net/s3/milab/2020/covid19-stat/data/v5/data-by-region/{}.json?v=1608969856500'.format(
            n_d[country]))
    data2 = json.loads(r2.text)

    today_country_cl = data2['cases'][-1][1]
    total_country_cl = data2['cases'][-1][0]

    today_country_dead = data2['deaths'][-1][1]
    total_country_dead = data2['deaths'][-1][0]

    cluch2 = 'й'
    if str(today_country_cl)[-1] in ['2', '3', '4']:
        cluch2 = 'я'
    if str(today_country_cl)[-1] in ['5', '6', '7', '8', '9', '0']:
        cluch2 = 'ев'

    city = d[int(city)].split()
    city = '%20'.join(city)

    f = requests.get('https://ws3.morpher.ru/russian/declension?s={}&format=json'.format(city))
    data_morph = json.loads(f.text)

    title1 = "В {} выявлен{} {} новы{} случа{} заражения коронавирусом<br><br>".format(data_morph['П'], viyavleno,
                                                                                       today_sl, novix, cluchaev)
    if today_dead == 0:
        today_dead = '0'

    if today_dead != 0:
        t_skonch = 'ось'
        if str(today_dead)[-1] == '1':
            t_skonch = 'ся'
        pacient = ''
        if str(today_dead)[-1] in ['2', '3', '4']:
            pacient = 'а'
        if str(today_dead)[-1] in ['5', '6', '7', '8', '9', '0']:
            pacient = 'ов'

        title2 = "В {} скончал{} {} пациент{} с коронавирусом<br><br>".format(data_morph['П'], t_skonch, today_dead,
                                                                              pacient)
    title = title1 if today_dead == '0' else random.choice([title1, title2])

    date = str(datetime.datetime.now().strftime("%d.%m.%Y"))

    month = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
             'Декабря'][int(date.split('.')[1]) - 1].lower()
    n_dayweek = datetime.datetime.today().weekday()
    dayweek = ['понедельник', "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"][n_dayweek]
    day = date.split('.')[0]
    date = dayweek + ' ' + day + ' ' + month

    article = "В {} в {} выявлен{} {} новы{} случа{} заражения COVID-19. {}. Об этом сообщает столичный оперштаб." \
              "<br><br>Всего с начала пандемии в регионе жертвами коронавируса стали {} человек{}, общее число случаев заражения составило {}." \
              "<br><br>В России за сутки выявили {} случа{} заражения (всего {}), умерло пациентов — {} (всего {})".format(
        date, data_morph['П'], viyavleno, today_sl, novix, cluchaev, today_dead_a,
        total_reg_dead, cheloveka, total_reg_sl, today_country_cl, cluch2, total_country_cl,
        today_country_dead, total_country_dead)

    l = []
    for i in data['cases']:
        l.append(i[1])

    l2 = []
    for i in data['deaths']:
        l2.append(i[1])

    today = datetime.datetime.now()

    DD = datetime.timedelta(days=len(data2['cases']) - 1)
    earlier = today - DD
    earlier_str = str(earlier.strftime("%Y.%m.%d"))

    l_d = []
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date(*[int(i) for i in earlier_str.split('.')])
    end_date = datetime.date.today()
    for i in range((end_date - start_date).days + 1):
        r = start_date + i * day_delta
        dat = r.strftime("%d.%m")
        l_d.append(str(dat))

    trace = go.Scatter(
        x=l_d,
        y=l,
        mode='lines',
        line=dict(width=3, shape='spline', smoothing=1.3),
        fillcolor='rgba(0,100,80,0.2)',
        marker=dict(
            color='rgb(226,83,221)',
            size=202,
            line=dict(
                color='MediumPurple',
                width=2,
                colorscale="Cividis",
            )
        ),
    )
    layout = go.Layout(
        title='<b>Динамика случаев заражения коронавирусом <br>в {}</b>'.format(data_morph['П']),
        titlefont=dict(
            size=20,
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title='Дата',
            titlefont=dict(
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Число случаев',
            titlefont=dict(
                size=18,
                color='#7f7f7f'
            )

        )
    )
    fig = go.Figure(data=[trace], layout=layout, )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(153,153,255, 0.7)')
    fig.update_layout(hovermode="x")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        )
    )
    fig.update(layout=dict(title=dict(x=0.5)))
    div = plotly.io.to_html(fig, full_html=False, config=dict(displayModeBar=False))

    trace2 = go.Scatter(
        x=l_d,
        y=l2,
        mode='lines',
        line=dict(width=3, shape='spline', smoothing=1.3),
        fillcolor='rgba(0,100,80,0.2)',
        marker=dict(
            color='rgb(102, 102, 102)',
            size=202,
            line=dict(
                color='MediumPurple',
                width=2,
                colorscale="Cividis",
            )
        ),
    )
    layout2 = go.Layout(
        title='<b>Динамика смертей от коронавируса <br>в {}</b>'.format(data_morph['П']),
        titlefont=dict(
            size=20,
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title='Дата',
            titlefont=dict(
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Число смертей',
            titlefont=dict(
                size=18,
                color='#7f7f7f'
            )

        )
    )
    fig2 = go.Figure(data=[trace2], layout=layout2, )
    fig2.update_xaxes(showgrid=False)
    fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(153,153,255, 0.7)')
    fig2.update_layout(hovermode="x")
    fig2.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        )
    )
    fig2.update(layout=dict(title=dict(x=0.5)))
    div2 = plotly.io.to_html(fig2, full_html=False, config=dict(displayModeBar=False))

except Exception:

    title = ''
    article = 'Данных за сегодняшний день, {}, нет.'.format(datetime.datetime.today().strftime("%d.%m.%Y"))
    div = ''
    div2 = ''

if data['info']['date'] == datetime.datetime.today().strftime('%Y-%m-%d'):
    data = {}
    data['result'] = '<h2>{}</h2>'.format(title) + '<p>{}</p>'.format(article) + div + div2

else:
    data = {}
    data['result'] = 'Данных за сегодняшний день, {}, нет.'.format(datetime.datetime.today().strftime("%d.%m.%Y"))
